# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Body(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location: float=None):
        """
        Body - a model defined in Swagger

        :param location: The location of this Body.
        :type location: float
        """
        self.swagger_types = {
            'location': float
        }

        self.attribute_map = {
            'location': 'location'
        }

        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.
        :rtype: Body
        """
        return deserialize_model(dikt, cls)

    @property
    def location(self) -> float:
        """
        Gets the location of this Body.

        :return: The location of this Body.
        :rtype: float
        """
        return self._location

    @location.setter
    def location(self, location: float):
        """
        Sets the location of this Body.

        :param location: The location of this Body.
        :type location: float
        """

        self._location = location
