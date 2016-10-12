"""The restless Serializer for the models."""
from restless.serializers import JSONSerializer
from dokomoforms.models import ModelJSONEncoder
import json


class ModelJSONSerializer(JSONSerializer):

    """Drop-in replacement for the restless-supplied JSONSerializer.

    Uses dokomo's ModelJSONEncoder in order to correctly serialize models
    to JSON.
    """

    def serialize(self, data):
        """The low-level serialization.

        Underpins ``serialize``, ``serialize_list`` &
        ``serialize_detail``.
        Has no built-in smarts, simply dumps the JSON.
        :param data: The body for the response
        :type data: string
        :returns: A serialized version of the data
        :rtype: string
        """
        for chunk in ModelJSONEncoder().iterencode(data):
            yield chunk.replace('</', '<\\/')
        #return json.dumps(data, cls=ModelJSONEncoder).replace('</', '<\\/')
