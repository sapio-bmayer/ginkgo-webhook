from sapiopylib.rest.WebhookService import WebhookConfiguration, WebhookServerFactory


from webhook.hello_world import HelloWorldWebhookHandler
from waitress import serve

from webhook.lock_experiment import LockExperimentWebhookHandler
from webhook.populate_list import PopulateListWebhookHandler

# Create the Sapio webhook configuration that will handle the processing of
config: WebhookConfiguration = WebhookConfiguration(verify_sapio_cert=False, debug=True)
config.register('/hello_world', HelloWorldWebhookHandler)
config.register('/populate_list', PopulateListWebhookHandler)
config.register('/lock_experiment', LockExperimentWebhookHandler)
# config.register('/create_details', HelloWorldWebhookHandler)  # TODO


# Create a flask application with the Sapio Webhook configuration
app = WebhookServerFactory.configure_flask_app(app=None, config=config)


# Return the README.md file as a html file for the homepage of the webhook
@app.route('/')
def http_root():
    import markdown
    readme_file = open('README.md')
    output = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style type="text/css">
"""
    output += open('doc/avenir-white.css').read()
    output += "</style></head><body>"
    output += markdown.markdown(readme_file.read())
    output += "</body></html>"
    return output


# This method is a health check for render.com to use to know when the python process is alive and is healthy
@app.route('/health_check')
def health_check():
    return 'Alive'


# UNENCRYPTED! This should not be used in production. You should give the "app" a ssl_context or set up a reverse-proxy.
serve(app, host="0.0.0.0", port=8090)
