import markdownify
from bs4 import BeautifulSoup
from models import EmailSchema

class EmailProcessor:
    @staticmethod
    def to_markdown(email: EmailSchema) -> str:
        # Clean HTML first
        soup = BeautifulSoup(email.body, "html.parser")
        clean_html = str(soup)
        
        # Convert to Markdown
        md_content = markdownify.markdownify(clean_html, heading_style="ATX")
        
        final_output = f"""
        Subject: {email.subject}
        Sender: {email.sender}
        Date: {email.received_at}
        
        Body:
        {md_content}
        """
        return final_output