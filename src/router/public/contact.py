from src.interfaces import AWS
from src.models.agents import Contact, Contacts
from fastapi import APIRouter, HTTPException, Depends

ses = AWS.get_client("ses")


contact = APIRouter()

def send_email(contact: Contact):
    try:
        ses.send_email(
            Source=ses.env.AWS_SES_MAIL_FROM,
            Destination={
                "ToAddresses": [
                    ses.env.AWS_SES_MAIL_TO
                ]
            },
            Message={
                "Subject": {
                    "Data": f"{contact.displayName}<{contact.email}>"
                },
                "Body": {
                    "Text": {
                        "Data": contact.message
                    }   
                }
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return contact




