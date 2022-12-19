class PaginationHelper:
    """
    A helper class for dealing with paginated requests.
    """

    def __init__(
        self, input_token, output_token, result_key, limit_key=None, more_results=None, non_aggregate_keys=None
    ):
        self.input_token = input_token
        self.output_token = output_token
        self.result_key = result_key
        self.limit_key = limit_key
        self.more_results = more_results
        self.non_aggregate_keys = non_aggregate_keys
        self.keys_to_remove = []
        self.keys_to_remove.extend(input_token)
        self.keys_to_remove.extend(output_token)
        if more_results:
            self.keys_to_remove.append(self.more_results)

    def remove_keys(self, params):
        """
        Remove pagination related keys from output parameters.
        :param params: params.
        :return: None
        """
        for k in self.keys_to_remove:
            params.pop(k, None)

    def handle_pagination(self, input_, output):
        """
        Looks at the output of a rest call and determines if the call was paginated.

        :param input: The input variables
        :param output: The output variables
        :return: True if more results are available, False otherwise
        """
        is_paginated = False

        # It seems that is never being executed.
        if self.more_results and self.more_results in output.keys() and output[self.more_results]:
            is_paginated = True

        for idx, _ in enumerate(self.input_token):
            if self.output_token[idx] in output.keys():
                input_[self.input_token[idx]] = output[self.output_token[idx]]
                is_paginated = True

        return is_paginated

    def merge_responses(self, input_, a, b):
        """
        Merges two output dictionaries together.
        :param input:
        :param a:
        :param b:
        :return:
        """
        max_hit = False

        for r in self.result_key:
            c = a[r]
            a[r] = b[r]
            a[r].extend(c)

            if self.limit_key and self.limit_key in input_.keys():
                if len(a[r]) >= input_[self.limit_key]:
                    max_hit = True
                    a[r] = a[r][: input_[self.limit_key]]

        return a, max_hit
