from fastapi_mail import FastMail,MessageSchema ,MessageType
from app.core.logging import get_logger
from app.utils.mail_config import conf
logger = get_logger()

class EmailService:
    def __init__(self):
        self.fm = FastMail(conf)
    
    async def send_email(self,recipients:list[str],subject:str,body:str):
        logger.info(f"EmailService: send_email called with recipients: {recipients}, subject: {subject}, body: {body}")
        message = MessageSchema(
            subject = subject,
            recipients = recipients,
            body = body
        )
        try:
          result = await self.fm.send_message(message)
        except Exception as e:
           logger.error("Failed To Send Email")