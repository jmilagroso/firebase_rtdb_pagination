import math
import sys


class FirebaseRTDBPagination:

    def __init__(
            self,
            firebase_admin_db,
            path,
            child_key,
            sort_by='desc',
            per_page=25):

        # Firebase RealtimeDB firebase_admin db
        self.firebase_admin_db = firebase_admin_db

        # Firebase RealtimeDB database path
        self.path = path

        # Firebase RealtimeDB child key
        self.child_key = child_key

        # Sort mechanism (desc or asc)
        self.sort_by = sort_by

        # Number of records per page
        self.per_page = per_page

        # Min value for matching int
        self.min_value = -1
        # Max value for matching int.
        # An integer giving the maximum value a variable of type
        # Py_ssize_t can take. It’s usually 2^31 - 1 on a 32-bit
        # platform and 2^63 - 1 on a 64-bit platform.
        self.max_value = sys.maxsize

        # Get Firebase RealtimeDB database reference
        self.ref = self.firebase_admin_db.reference(self.path)

    def all(self):
        # Return Firebase RealtimeDB records
        return self.ref.get()

    def get(self, cursor_last=None):
        # Latest Firebase RealtimeDB record count
        self.count = len(self.ref.get())

        # Firebase RealtimeDB query instance
        self.query = self.ref.order_by_child(self.child_key)

        # Total number of pages
        pages = math.ceil(self.count / self.per_page)

        # Handle out of range pagination, returns empty
        if isinstance(
                cursor_last,
                list) and cursor_last == []:
            return {
                'data': [],
                'cursor': [],
                'pages': pages,
                'total': self.count
            }

        if self.sort_by == 'desc':
            # Firebase RealtimeDB descending query handling
            if cursor_last is None:
                cursor_last = self.max_value

            self.query = self.query.end_at(cursor_last - 1) \
                .limit_to_last(self.per_page)
        else:
            # Firebase RealtimeDB ascending query handling
            if cursor_last is None:
                cursor_last = self.min_value

            self.query = self.query.start_at(
                cursor_last + 1) \
                .limit_to_first(self.per_page)

        data = self.__sort(
            self.__format(
                self.query.get()
            )
        )

        return {
            'data': data,
            'cursor': data[len(data) - 1].get(self.child_key) if data else [],
            'pages': pages,
            'total': self.count
        }

    def __sort(self, data):

        # Determine sorting based on sort_by parameter

        is_reversed = True if self.sort_by == 'desc' else False

        return sorted(
            data,
            key=lambda k: k[self.child_key],
            reverse=is_reversed
        )

    def __format(self, data):
        # Format Firebase RealtimeDB record output
        # into standardised array of dict

        result = []

        if isinstance(data, list):
            result = [i for i in data if i] \
                if len(data) > 1 else [data[0]]
        else:
            if data:
                dict_data = dict(data)
                result = [dict_data.get(i) for i in dict_data if i]

        return result
