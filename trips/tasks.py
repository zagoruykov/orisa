import time

from huey.contrib.djhuey import HUEY as huey


@huey.task()
def run_template(template_data, template_id=None):
    time.sleep(60)
    return f'Template {template_data}#{template_id} has been started successfully'
