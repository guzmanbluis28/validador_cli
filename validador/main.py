import argparse
import logging
from .utils import is_valid_email, is_valid_url

logging.basicConfig(level=logging.INFO)

def run():
        parser = argparse.ArgumentParser(description="Validador de emails y URLs")
        parser.add_argument("--email", type=str, help="Email a validar")
        parser.add_argument("--url", type=str, help="URL a validar")
        args = parser.parse_args()

        if args.email:
            if is_valid_email(args.email):
                logging.info("Email válido")
            else:
                logging.warning("Email inválido")

        if args.url:
            if is_valid_url(args.url):
                logging.info("URL válida")
            else:
                logging.warning("URL inválida")
