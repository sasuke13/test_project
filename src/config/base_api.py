from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class ApiBaseView:
    def __serialize_list(self, lst: list, serializer: Serializer()) -> list:
        serialized_values = []

        for item in lst:
            serialized_values.append(serializer(item).data)

        return serialized_values

    def _serialize_dict(self, data: dict, serializer: Serializer()):

        for key, value in data.items():
            data[key] = self.__serialize_list(data[key], serializer)

    def _serialize_nested_dict(self, data: dict, serializer: Serializer()):
        for key, value in data.items():
            for item in data[key]:
                for nested_key, nested_value in item.items():
                    item[nested_key] = self.__serialize_list(item[nested_key], serializer)

    def _create_response_for_invalid_serializers(self, *serializers):
        errors = {}
        for serializer in serializers:
            if isinstance(serializer, type):
                serializer_instance = serializer(data=self.request.data)
            else:
                serializer_instance = serializer
            serializer_instance.is_valid()
            serializer_errors = serializer_instance.errors
            if serializer_errors:
                errors.update(serializer_errors)
            print(errors)
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

    def _create_response_for_exception(self, exception):
        return Response({"error": str(exception)}, status=status.HTTP_400_BAD_REQUEST)

    def _create_response_not_found(self, exception):
        return Response({"error": str(exception)}, status=status.HTTP_404_NOT_FOUND)
