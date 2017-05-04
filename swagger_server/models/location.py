# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Location(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, location: float=None):
        """
        Location - a model defined in Swagger

        :param location: The location of this Location.
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
    def from_dict(cls, dikt) -> 'Location':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Location of this Location.
        :rtype: Location
        """
        return deserialize_model(dikt, cls)

    @property
    def location(self) -> float:
        """
        Gets the location of this Location.

        :return: The location of this Location.
        :rtype: float
        """
        return self._location

    @location.setter
    def location(self, location: float):
        """
        Sets the location of this Location.

        :param location: The location of this Location.
        :type location: float
        """

        self._location = location
