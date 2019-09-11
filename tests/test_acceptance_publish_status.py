import pytest

from common.base import Login
from common.helpers import verify_status_posted, add_status_text, add_status_image


@pytest.mark.acceptance
class AcceptanceTestFBPublishStatus(Login):

    def test_publish_status_text_only(self, now):
        add_status_text(self.driver, "Automated test {now}".format(now=now), publish=True)
        verify_status_posted(self.driver, now)

    def test_publish_status_image_only(self, image_attachment):
        add_status_image(self.driver, image=image_attachment, publish=True)
        verify_status_posted(self.driver, image=image_attachment)
