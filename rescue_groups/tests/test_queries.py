from rescue_groups.utils.db_ops import save_animal

from unittest import mock

import unittest
import json


class TestDBOperations(unittest.TestCase):
    """Test db operations"""

    @mock.patch("rescue_groups.utils.db_ops.animal_by_id_req")
    @mock.patch("rescue_groups.utils.db_ops.flask")
    @mock.patch("rescue_groups.utils.db_ops.current_user")
    def test_save_animal(
        self,
        mock_current_user: mock.MagicMock(),
        mock_flask: mock.MagicMock(),
        mock_animal_by_id: mock.MagicMock(),
    ):
        """Test saves animal to animals table"""
        # Given
        # Create mock session
        mock_session = mock.MagicMock()
        mock_flask.g.session = mock_session
        # Mock rescue group api query result
        mock_animal_by_id.return_value = json.dumps({
            "data": {
                "1": {
                    "animalID": 1,
                    "userID": 1,
                    "locationPostalcode": "location",
                    "animalEyeColor": "eye_color",
                    "animalColor": "color",
                    "animalName": "name",
                    "animalDescription": "description",
                    "animalGeneralAge": "age",
                    "animalSex": "sex",
                    "animalThumbnailUrl": "thumbnail",
                }
            }
        })

        # When
        # Call save animal function that we are testing
        save_animal(1)

        # Then
        # Make sure everything is called and committed to DB
        mock_animal_by_id.assert_called_with("rescue_group", 1)
        mock_flask.g.session.add.assert_called_once()
        mock_flask.g.session.commit.assert_called_once()

