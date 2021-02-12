# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.date_offset_config import DateOffsetConfig
from openapi_server.models.masking_char_config import MaskingCharConfig
from openapi_server import util

from openapi_server.models.date_offset_config import DateOffsetConfig  # noqa: E501
from openapi_server.models.masking_char_config import MaskingCharConfig  # noqa: E501

class DeidentificationStep(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, confidence_threshold=0, masking_char_config=None, annotation_type_mask_config=None, redact_config=None, date_offset_config=None, annotation_types=None):  # noqa: E501
        """DeidentificationStep - a model defined in OpenAPI

        :param confidence_threshold: The confidence_threshold of this DeidentificationStep.  # noqa: E501
        :type confidence_threshold: float
        :param masking_char_config: The masking_char_config of this DeidentificationStep.  # noqa: E501
        :type masking_char_config: MaskingCharConfig
        :param annotation_type_mask_config: The annotation_type_mask_config of this DeidentificationStep.  # noqa: E501
        :type annotation_type_mask_config: object
        :param redact_config: The redact_config of this DeidentificationStep.  # noqa: E501
        :type redact_config: object
        :param date_offset_config: The date_offset_config of this DeidentificationStep.  # noqa: E501
        :type date_offset_config: DateOffsetConfig
        :param annotation_types: The annotation_types of this DeidentificationStep.  # noqa: E501
        :type annotation_types: List[str]
        """
        self.openapi_types = {
            'confidence_threshold': float,
            'masking_char_config': MaskingCharConfig,
            'annotation_type_mask_config': object,
            'redact_config': object,
            'date_offset_config': DateOffsetConfig,
            'annotation_types': List[str]
        }

        self.attribute_map = {
            'confidence_threshold': 'confidenceThreshold',
            'masking_char_config': 'maskingCharConfig',
            'annotation_type_mask_config': 'annotationTypeMaskConfig',
            'redact_config': 'redactConfig',
            'date_offset_config': 'dateOffsetConfig',
            'annotation_types': 'annotationTypes'
        }

        self._confidence_threshold = confidence_threshold
        self._masking_char_config = masking_char_config
        self._annotation_type_mask_config = annotation_type_mask_config
        self._redact_config = redact_config
        self._date_offset_config = date_offset_config
        self._annotation_types = annotation_types

    @classmethod
    def from_dict(cls, dikt) -> 'DeidentificationStep':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeidentificationStep of this DeidentificationStep.  # noqa: E501
        :rtype: DeidentificationStep
        """
        return util.deserialize_model(dikt, cls)

    @property
    def confidence_threshold(self):
        """Gets the confidence_threshold of this DeidentificationStep.

        The minimum confidence level for a given annotation to be de-identified  # noqa: E501

        :return: The confidence_threshold of this DeidentificationStep.
        :rtype: float
        """
        return self._confidence_threshold

    @confidence_threshold.setter
    def confidence_threshold(self, confidence_threshold):
        """Sets the confidence_threshold of this DeidentificationStep.

        The minimum confidence level for a given annotation to be de-identified  # noqa: E501

        :param confidence_threshold: The confidence_threshold of this DeidentificationStep.
        :type confidence_threshold: float
        """
        if confidence_threshold is not None and confidence_threshold > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence_threshold`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence_threshold is not None and confidence_threshold < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence_threshold = confidence_threshold

    @property
    def masking_char_config(self):
        """Gets the masking_char_config of this DeidentificationStep.


        :return: The masking_char_config of this DeidentificationStep.
        :rtype: MaskingCharConfig
        """
        return self._masking_char_config

    @masking_char_config.setter
    def masking_char_config(self, masking_char_config):
        """Sets the masking_char_config of this DeidentificationStep.


        :param masking_char_config: The masking_char_config of this DeidentificationStep.
        :type masking_char_config: MaskingCharConfig
        """

        self._masking_char_config = masking_char_config

    @property
    def annotation_type_mask_config(self):
        """Gets the annotation_type_mask_config of this DeidentificationStep.

        Configuration for the \"annotation type\" strategy. E.g. \"John Smith lives at 123 Main St\" -> \"[PERSON_NAME] lives at [PHYSICAL_ADDRESS]\".  # noqa: E501

        :return: The annotation_type_mask_config of this DeidentificationStep.
        :rtype: object
        """
        return self._annotation_type_mask_config

    @annotation_type_mask_config.setter
    def annotation_type_mask_config(self, annotation_type_mask_config):
        """Sets the annotation_type_mask_config of this DeidentificationStep.

        Configuration for the \"annotation type\" strategy. E.g. \"John Smith lives at 123 Main St\" -> \"[PERSON_NAME] lives at [PHYSICAL_ADDRESS]\".  # noqa: E501

        :param annotation_type_mask_config: The annotation_type_mask_config of this DeidentificationStep.
        :type annotation_type_mask_config: object
        """

        self._annotation_type_mask_config = annotation_type_mask_config

    @property
    def redact_config(self):
        """Gets the redact_config of this DeidentificationStep.

        Configuration for the redaction strategy. E.g. \"John Smith lives at 123 Main St\" -> \"lives at\".  # noqa: E501

        :return: The redact_config of this DeidentificationStep.
        :rtype: object
        """
        return self._redact_config

    @redact_config.setter
    def redact_config(self, redact_config):
        """Sets the redact_config of this DeidentificationStep.

        Configuration for the redaction strategy. E.g. \"John Smith lives at 123 Main St\" -> \"lives at\".  # noqa: E501

        :param redact_config: The redact_config of this DeidentificationStep.
        :type redact_config: object
        """

        self._redact_config = redact_config

    @property
    def date_offset_config(self):
        """Gets the date_offset_config of this DeidentificationStep.


        :return: The date_offset_config of this DeidentificationStep.
        :rtype: DateOffsetConfig
        """
        return self._date_offset_config

    @date_offset_config.setter
    def date_offset_config(self, date_offset_config):
        """Sets the date_offset_config of this DeidentificationStep.


        :param date_offset_config: The date_offset_config of this DeidentificationStep.
        :type date_offset_config: DateOffsetConfig
        """

        self._date_offset_config = date_offset_config

    @property
    def annotation_types(self):
        """Gets the annotation_types of this DeidentificationStep.

        The types of annotations to which the de-identifer should apply the selected strategy  # noqa: E501

        :return: The annotation_types of this DeidentificationStep.
        :rtype: List[str]
        """
        return self._annotation_types

    @annotation_types.setter
    def annotation_types(self, annotation_types):
        """Sets the annotation_types of this DeidentificationStep.

        The types of annotations to which the de-identifer should apply the selected strategy  # noqa: E501

        :param annotation_types: The annotation_types of this DeidentificationStep.
        :type annotation_types: List[str]
        """
        allowed_values = ["text_physical_address", "text_date", "text_person_name"]  # noqa: E501
        if not set(annotation_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `annotation_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(annotation_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._annotation_types = annotation_types
