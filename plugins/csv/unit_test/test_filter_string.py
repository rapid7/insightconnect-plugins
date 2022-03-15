import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_csv.actions.filter_string import FilterString
from komand_csv.actions.filter_string.schema import Input, Output


class TestFilterString(TestCase):
    def setUp(self) -> None:
        self.action = FilterString()

    def test_filter_string(self):
        actual = self.action.run(
            {
                Input.CSV: "seq,name/first,name/last,age,street,city,state,zip,dollar,pick,date\n"
                "1,Craig,Goodman,44,Ezazeh Key,Ehamaklu,NM,73494,$8986.62,YELLOW,08/20/2006\n"
                "2,Isaac,Vega,48,Domuna Junction,Edevomov,OR,95511,$8167.38,WHITE,12/14/1963\n"
                "3,Vera,Duncan,30,Duler Highway,Jusavimij,DE,20194,$98.44,RED,03/06/1954\n"
                "4,Ricardo,Sharp,57,Javuz Manor,Ijkiiha,HI,17218,$79.67,BLUE,04/17/1965\n"
                "5,Bruce,Stephens,37,Iweuta Place,Focjele,UT,27512,$492.30,GREEN,12/20/1956\n"
                "6,Bettie,Rios,59,Pucev Center,Gabuva,CT,72681,$1085.18,YELLOW,09/12/1973",
                Input.FIELDS: "f2, f4-f5",
            }
        )
        expected = {
            Output.STRING: "name/first,age,street\nCraig,44,Ezazeh Key\nIsaac,48,Domuna Junction\nVera,30,Duler Highway\nRicardo,57,Javuz Manor\nBruce,37,Iweuta Place\nBettie,59,Pucev Center"
        }
        self.assertEqual(actual, expected)

    def test_filter_string_empty_csv(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "",
                    Input.FIELDS: "f1",
                }
            )

        self.assertEqual(e.exception.cause, "CSV input is empty.")
        self.assertEqual(e.exception.assistance, "Please provide a valid CSV input.")

    def test_filter_string_empty_fields(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "seq,name/first,name/last,age,street,city,state,zip,dollar,pick,date\n"
                    "1,Craig,Goodman,44,Ezazeh Key,Ehamaklu,NM,73494,$8986.62,YELLOW,08/20/2006\n",
                    Input.FIELDS: "",
                }
            )

        self.assertEqual(e.exception.cause, "Empty fields input.")
        self.assertEqual(e.exception.assistance, "Please provide valid fields.")

    def test_filter_string_invalid_fields_syntax(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "seq,name/first,name/last,age,street,city,state,zip,dollar,pick,date\n"
                    "1,Craig,Goodman,44,Ezazeh Key,Ehamaklu,NM,73494,$8986.62,YELLOW,08/20/2006\n",
                    Input.FIELDS: "g3",
                }
            )

        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Improper syntax in fields string.")

    def test_filter_string_invalid_fields(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: "seq,name/first,name/last,age,street,city,state,zip,dollar,pick,date\n"
                    "1,Craig,Goodman,44,Ezazeh Key,Ehamaklu,NM,73494,$8986.62,YELLOW,08/20/2006\n",
                    Input.FIELDS: "f22",
                }
            )

        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Invalid field indices.")

    def test_filter_string_value_as_array(self):
        actual = self.action.run(
            {
                Input.CSV: 'column1,column2,column3\nvalue1, value2, value3\n value4,"[value, value]", value6\n',
                Input.FIELDS: "f2",
            }
        )
        expected = {Output.STRING: "column2\nvalue2\n[value, value]"}

        self.assertEqual(actual, expected)

    def test_filter_string_empty_values(self):
        actual = self.action.run(
            {Input.CSV: "column1,column2,column3\n, value2, value3\n value4,, value6\n", Input.FIELDS: "f2"}
        )
        expected = {Output.STRING: "column2\nvalue2\n"}
        self.assertEqual(actual, expected)

    def test_filter_string_unicode(self):
        actual = self.action.run(
            {Input.CSV: "column1,column2,column3\n, pythöö, value3\n value4,ąaćceę, value6\n", Input.FIELDS: "f2"}
        )
        expected = {Output.STRING: "column2\npythöö\nąaćceę"}
        self.assertEqual(actual, expected)

    def test_filter_string_invalid_csv_syntax(self):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.CSV: 'column1,column2gbnm\nvalue1, value2, value3\n value4,"[value, value]", value6\n',
                    Input.FIELDS: "f2",
                }
            )
        self.assertEqual(e.exception.cause, "Wrong input.")
        self.assertEqual(e.exception.assistance, "Improper syntax in CSV string.")
