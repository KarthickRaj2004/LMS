# courses/views.py

from django.shortcuts import render, get_object_or_404
from .models import Course  # Import Course model
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')
def course_list(request):
    main_courses = Course.objects.filter(main_course=None)
    return render(request, 'course_list.html', {'courses': main_courses})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        if name and email and subject and message:
            send_mail(
                'Contact Form Submission',
                f'Sender: {name}\nEmail: {email}\n\n{message}',
                'settings.EMAIL_HOST_USER',  # Change this to your actual email host user
                [email],  # Assuming you want to send an email to the user who submitted the form
                fail_silently=False
            )
            return render(request, "contact.html", {'message': 'Thank you for your message! We will get back to you soon.'})
        else:
            return render(request, "contact.html", {'error_message': 'Please fill out all the fields.'})
    return render(request, "contact.html")


def course_detail(request, course_id):
    main_course = get_object_or_404(Course, pk=course_id)
    sub_courses = main_course.sub_courses.all()
    return render(request, 'sub_course_list.html', {'main_course': main_course, 'sub_courses': sub_courses})

def sub_course_detail(request, sub_course_id):
    sub_course = get_object_or_404(Course, pk=sub_course_id)
    learning_modules = sub_course.learning_modules.all()
    powerpoint_presentations = sub_course.powerpoint_presentations.all()
    return render(request, 'sub_course_detail.html', {'sub_course': sub_course, 'learning_modules': learning_modules, 'powerpoint_presentations': powerpoint_presentations})

# courses/views.py

from django.shortcuts import render
from django.conf import settings
import razorpay

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def payment_page(request):
    currency = 'INR'
    amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(
        amount=amount,
        currency=currency,
        payment_capture='0'
    ))

    # order id of newly created order
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # Pass the Razorpay key to the payment form template
    razorpay_key = settings.RAZOR_KEY_ID

    # Context data to be passed to the template
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_amount': amount,
        'currency': currency,
        'callback_url': callback_url,
        'razorpay_key': razorpay_key,  # Pass the Razorpay API key to the template
    }

    return render(request, 'payments/payment_form.html', context=context)

from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

def homepage(request):
	currency = 'INR'
	amount = 20000 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url

	return render(request, 'index.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()
