<<<<<<< HEAD:lwe/examples/functions/reverse_content.py
from chatgpt_wrapper.core.function import Function
=======
from lwe.core.tool import Tool
>>>>>>> 2fed83cbae5504ac804d96aa11c51033d3f0028a:lwe/examples/tools/reverse_content.py


class ReverseContent(Tool):
    def __call__(self, content: str) -> dict:
        """
        Reverse the provided content

        :param content: The content to reverse.
        :type content: str
        :return: A dictionary containing the reversed content.
        :rtype: dict
        """
        try:
            reversed_content = content[::-1]
            output = {
                "result": reversed_content,
                "message": "Reversed the content string",
            }
        except Exception as e:
            output = {
                "error": str(e),
            }
        return output
