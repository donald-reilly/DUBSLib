class SerializationError(Exception):
    """
    Base exception for all serialization errors.
    """

    pass

class UnsupportedFormatError(SerializationError):
    
    def __init__(self, format, supported_formats):
        """
        Unsupported serialization format.
    
        Params:
            format(module): The intended format of the serialized data.
            supported_formats(list[module]): A list of the supported formats.    
        """
        self.format = format

        self.supported_formats = tuple(supported_formats)

        error_message = (f"Unexpected format: {format!r} ." 
                         f"Expected one of; {', '.join(supported_formats)}")
        super().__init__(error_message)
