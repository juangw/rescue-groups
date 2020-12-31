from rescue_groups.utils.db_ops import save_animal

from unittest import mock

import unittest
import json


class TestDBOperations(unittest.TestCase):
    """Test db operations"""

    @mock.patch("rescue_groups.utils.db_ops.animal_by_id_req")
    @mock.patch("rescue_groups.utils.db_ops.session")
    @mock.patch("rescue_groups.utils.db_ops.current_user")
    def test_save_animal(
        self,
        mock_current_user: mock.MagicMock(),
        mock_session: mock.MagicMock(),
        mock_animal_by_id: mock.MagicMock(),
    ):
        """Test saves animal to animals table"""
        # Given
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
        # Mock current user id
        mock_current_user.id = None

        # When
        # Call save animal function that we are testing
        save_animal(1)

        # Then
        # Make sure everything is called and committed to DB
        mock_animal_by_id.assert_called_with("rescue_group", 1)
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()

