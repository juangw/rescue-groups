from common.utils.get_api_data import api_post_req

import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logger.debug("Start of Program, Testing Debugger")


def main():
    default_filter = [
        {
            "fieldName": "animalSpecies",
            "operation": "equals",
            "criteria": "cat"
        },
        {
            "fieldName": "animalLocation",
            "operation": "equals",
            "criteria": "48105"
        }
    ]
    default_fields = [
        "animalID",
        "animalOrgID",
        "locationPhone",
        "animalName",
        "animalThumbnailUrl",
        "animalPictures",
        "animalSex",
        "animalAdoptionFee",
        "animalBreed",
        "animalColor",
        "animalEyeColor",
        "animalAgeString",
        "animalLocation",
        "animalAffectionate",
        "animalApartment",
        "animalIntelligent",
        "animalLap",
        "animalActivityLevel"
    ]

    text = api_post_req("rescue_group", default_filter, default_fields)
    print(text)


if __name__ == '__main__':
    main()
