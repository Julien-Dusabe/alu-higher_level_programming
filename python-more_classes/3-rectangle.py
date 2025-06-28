#!/usr/bin/python3
    def __str__(self):
        """Return a string representation of the rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)
