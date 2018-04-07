class Wine:
    """This is a class that stores the information on some wine."""

    def __init__(self, name: str, bottling_year: int, trade_mark: str, country: str, *annotations):
        """Constructor of the class Wine.

        :param name: The name of the wine.
        :type str.
        :param bottling_year: The year when this wine was bottled.
        :type int.
        :param trade_mark: Trade mark of the wine.
        :type str.
        :param country: The country where the wine was bottled.
        :type str.
        :param annotations: Some annotations for the wine.
        :type list of str.
        """
        self.name = name
        self.bottling_year = bottling_year
        self.trade_mark = trade_mark
        self.country = country
        self.annotation = annotations

    def age(self, now_year: int) -> int:
        """This method calculates the age of the wine.

        :param now_year: The year that is now.
        :type now_year: int.
        :return: int.
        """
        return now_year - self.bottling_year
