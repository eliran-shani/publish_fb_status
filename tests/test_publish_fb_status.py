import pytest

from common.base import Login
from common.helpers import verify_status_posted, add_status_text, add_status_image


@pytest.fixture(scope="module")
def image():
    return "image.jpg"


class AcceptanceTestFBPublishStatus(Login):

    def test_publish_status_text_only(self, now):
        add_status_text(self.driver, "Automated test {now}".format(now=now), publish=True)
        verify_status_posted(self.driver, now)

    def test_publish_status_image_only(self, image):
        add_status_image(self.driver, image=image, publish=True)
        verify_status_posted(self.driver, image=image)


class TestFBPublishStatusOptional(AcceptanceTestFBPublishStatus):
    pass

    # TODO - Add feeling

    # TODO - Check - in

    # TODO - Tag friends

    # TODO - Add live stream

    # TODO - Add GIF

    # TODO - Recommendation

    # TODO - Watch party
