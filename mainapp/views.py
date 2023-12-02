from django.shortcuts import render
from .models import Purchase
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
import pdfkit
from io import BytesIO
from .serializers import PurchaseSerializers
from rest_framework import viewsets

def home(request):
    data = Purchase.objects.all()
    return render(request,'index.html',{'data':data})

def view_bill(request, user_id):
    user = Purchase.objects.get(id=user_id)
    return render(request, 'bill.html', {'user': user})

def Send_mail(request):
    if request.method == 'POST':
        try:
            userID = request.POST.get('userID')
            user = get_object_or_404(Purchase, id=userID)
            
            data = {
                'customer_name': user.customer_name,
                'customer_address': user.customer_address,
                'order_date': user.order_date,
                'product_name': user.product_name,
                'product_price': user.product_price,
                'quantity': user.quantity,
                'subtotal': user.subtotal,
            }

            html_content = render_to_string('pdf bill.html', data)

            pdf_content = pdfkit.from_string(html_content, False)
            pdf_file = BytesIO(pdf_content)
            pdf_file.seek(0)

            subject = 'Purchase Confirmation'
            email = EmailMessage(subject,
                                """Hi {},

I hope this message finds you well. We wanted to reach out and say a big thank you for choosing our company for your recent purchase of {}.

We truly appreciate your trust in us, and we're delighted to have you as our customer. If you have any questions or if there's anything we can assist you with regarding your new product, please feel free to let us know.

We're here to make sure you have a great experience with our product. Thanks again for your purchase, and we look forward to serving you in the future.

Best regards,""".format(user.customer_name, user.product_name),
                                to=[user.customer_email])
            email.attach('Purchase Bill.pdf', pdf_file.read(), 'application/pdf')
            email.send()

            return JsonResponse({'status': True})
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'status': False, 'error': str(e)})

    return JsonResponse({'status': False, 'error': 'Invalid request method'})

class PurchaseViewset(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializers