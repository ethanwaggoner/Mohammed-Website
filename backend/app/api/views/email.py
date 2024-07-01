from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail


class ContactFormViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        # This can return a simple message or any other information you want
        return Response({"message": "This is the contact form endpoint. Use the /send/ endpoint to submit the form."})

    @action(detail=False, methods=['post'], url_path='send', url_name='send-email')
    def send(self, request):
        first_name = request.data.get('firstName')
        last_name = request.data.get('lastName')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        if not all([first_name, last_name, email, subject, message]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        full_name = f"{first_name} {last_name}"
        email_message = f"From: {full_name} <{email}>\n\nMessage:\n{message}"

        send_mail(
            subject,
            email_message,
            email,  # Replace with your email
            ['ethanjwaggoner@gmail.com'],  # Replace with the recipient's email
            fail_silently=False,
        )

        return Response({"success": "Email sent successfully"}, status=status.HTTP_200_OK)
