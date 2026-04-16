import hashlib
import json
from collections import defaultdict
from html import unescape
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from autoscraper.utils import (
    FuzzyText,
    ResultItem,
    get_non_rec_text,
    normalize,
    text_match,
    unique_hashable,
    unique_stack_list,
)


class AutoScraper(object):
    """
    AutoScraper : A Smart, Automatic, Fast and Lightweight Web Scraper for Python.
    AutoScraper automatically learns a set of rules required to extract the needed content
        from a web page. So the programmer doesn't need to explicitly construct the rules.

    Attributes
    ----------
    stack_list: list
        List of rules learned by AutoScraper

    Methods
    -------
    build() - Learns a set of rules represented as stack_list based on the wanted_list,
        which can be reused for scraping similar elements from other web pages in the future.
    get_result_similar() - Gets similar results based on the previously learned rules.
    get_result_exact() - Gets exact results based on the previously learned rules.
    get_results() - Gets exact and similar results based on the previously learned rules.
    save() - Serializes the stack_list as JSON and saves it to disk.
    load() - De-serializes the JSON representation of the stack_list and loads it back.
    remove_rules() - Removes one or more learned rule[s] from the stack_list.
    keep_rules() - Keeps only the specified learned rules in the stack_list and removes the others.
    """

    request_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }

    def __init__(self, stack_list=None):
        self.stack_list = stack_list or []

    def save(self, file_path):
        """
        Serializes the stack_list as JSON and saves it to the disk.

        Parameters
        ----------
        file_path: str
            Path of the JSON output

        Returns
        -------
        None
        """
        pass

    def load(self, file_path):
        """
        De-serializes the JSON representation of the stack_list and loads it back.

        Parameters
        ----------
        file_path: str
            Path of the JSON file to load stack_list from.

        Returns
        -------
        None
        """
        pass

    @classmethod
    def _fetch_html(cls, url, request_args=None):
        pass

    @classmethod
    def _get_soup(cls, url=None, html=None, request_args=None):
        pass

    @staticmethod
    def _get_valid_attrs(item):
        pass

    @staticmethod
    def _child_has_text(child, text, url, text_fuzz_ratio):
        pass

    def _get_children(self, soup, text, url, text_fuzz_ratio):
        pass

    def build(
        self,
        url=None,
        wanted_list=None,
        wanted_dict=None,
        html=None,
        request_args=None,
        update=False,
        text_fuzz_ratio=1.0,
    ):
        """
        Automatically constructs a set of rules to scrape the specified target[s] from a web page.
            The rules are represented as stack_list.

        Parameters:
        ----------
        url: str, optional
            URL of the target web page. You should either pass url or html or both.

        wanted_list: list of strings or compiled regular expressions, optional
            A list of needed contents to be scraped.
                AutoScraper learns a set of rules to scrape these targets. If specified,
                wanted_dict will be ignored.

        wanted_dict: dict, optional
            A dict of needed contents to be scraped. Keys are aliases and values are list of target texts
                or compiled regular expressions.
                AutoScraper learns a set of rules to scrape these targets and sets its aliases.

        html: str, optional
            An HTML string can also be passed instead of URL.
                You should either pass url or html or both.

        request_args: dict, optional
            A dictionary used to specify a set of additional request parameters used by requests
                module. You can specify proxy URLs, custom headers etc.

        update: bool, optional, defaults to False
            If True, new learned rules will be added to the previous ones.
            If False, all previously learned rules will be removed.

        text_fuzz_ratio: float in range [0, 1], optional, defaults to 1.0
            The fuzziness ratio threshold for matching the wanted contents.

        Returns:
        --------
        List of similar results
        """
        pass

    @classmethod
    def _build_stack(cls, child, url):
        pass

    def _get_result_for_child(self, child, soup, url):
        pass

    @staticmethod
    def _fetch_result_from_child(child, wanted_attr, is_full_url, url, is_non_rec_text):
        pass

    @staticmethod
    def _get_fuzzy_attrs(attrs, attr_fuzz_ratio):
        pass

    def _get_result_with_stack(self, stack, soup, url, attr_fuzz_ratio, **kwargs):
        pass

    def _get_result_with_stack_index_based(
        self, stack, soup, url, attr_fuzz_ratio, **kwargs
    ):
        pass

    def _get_result_by_func(
        self,
        func,
        url,
        html,
        soup,
        request_args,
        grouped,
        group_by_alias,
        unique,
        attr_fuzz_ratio,
        **kwargs
    ):
        pass

    @staticmethod
    def _clean_result(
        result_list, grouped_result, grouped, grouped_by_alias, unique, keep_order
    ):
        pass

    def get_result_similar(
        self,
        url=None,
        html=None,
        soup=None,
        request_args=None,
        grouped=False,
        group_by_alias=False,
        unique=None,
        attr_fuzz_ratio=1.0,
        keep_blank=False,
        keep_order=False,
        contain_sibling_leaves=False,
    ):
        """
        Gets similar results based on the previously learned rules.

        Parameters:
        ----------
        url: str, optional
            URL of the target web page. You should either pass url or html or both.

        html: str, optional
            An HTML string can also be passed instead of URL.
                You should either pass url or html or both.

        request_args: dict, optional
            A dictionary used to specify a set of additional request parameters used by requests
                module. You can specify proxy URLs, custom headers etc.

        grouped: bool, optional, defaults to False
            If set to True, the result will be a dictionary with the rule_ids as keys
                and a list of scraped data per rule as values.

        group_by_alias: bool, optional, defaults to False
            If set to True, the result will be a dictionary with the rule alias as keys
                and a list of scraped data per alias as values.

        unique: bool, optional, defaults to True for non grouped results and
                False for grouped results.
            If set to True, will remove duplicates from returned result list.

        attr_fuzz_ratio: float in range [0, 1], optional, defaults to 1.0
            The fuzziness ratio threshold for matching html tag attributes.

        keep_blank: bool, optional, defaults to False
            If set to True, missing values will be returned as empty strings.

        keep_order: bool, optional, defaults to False
            If set to True, the results will be ordered as they are present on the web page.

        contain_sibling_leaves: bool, optional, defaults to False
            If set to True, the results will also contain the sibling leaves of the wanted elements.

        Returns:
        --------
        List of similar results scraped from the web page.
        Dictionary if grouped=True or group_by_alias=True.
        """
        pass

    def get_result_exact(
        self,
        url=None,
        html=None,
        soup=None,
        request_args=None,
        grouped=False,
        group_by_alias=False,
        unique=None,
        attr_fuzz_ratio=1.0,
        keep_blank=False,
    ):
        """
        Gets exact results based on the previously learned rules.

        Parameters:
        ----------
        url: str, optional
            URL of the target web page. You should either pass url or html or both.

        html: str, optional
            An HTML string can also be passed instead of URL.
                You should either pass url or html or both.

        request_args: dict, optional
            A dictionary used to specify a set of additional request parameters used by requests
                module. You can specify proxy URLs, custom headers etc.

        grouped: bool, optional, defaults to False
            If set to True, the result will be a dictionary with the rule_ids as keys
                and a list of scraped data per rule as values.

        group_by_alias: bool, optional, defaults to False
            If set to True, the result will be a dictionary with the rule alias as keys
                and a list of scraped data per alias as values.

        unique: bool, optional, defaults to True for non grouped results and
                False for grouped results.
            If set to True, will remove duplicates from returned result list.

        attr_fuzz_ratio: float in range [0, 1], optional, defaults to 1.0
            The fuzziness ratio threshold for matching html tag attributes.

        keep_blank: bool, optional, defaults to False
            If set to True, missing values will be returned as empty strings.

        Returns:
        --------
        List of exact results scraped from the web page.
        Dictionary if grouped=True or group_by_alias=True.
        """
        pass

    def get_result(
        self,
        url=None,
        html=None,
        request_args=None,
        grouped=False,
        group_by_alias=False,
        unique=None,
        attr_fuzz_ratio=1.0,
    ):
        """
        Gets similar and exact results based on the previously learned rules.

        Parameters:
        ----------
        url: str, optional
            URL of the target web page. You should either pass url or html or both.

        html: str, optional
            An HTML string can also be passed instead of URL.
                You should either pass url or html or both.

        request_args: dict, optional
            A dictionary used to specify a set of additional request parameters used by requests
                module. You can specify proxy URLs, custom headers etc.

        grouped: bool, optional, defaults to False
            If set to True, the result will be dictionaries with the rule_ids as keys
                and a list of scraped data per rule as values.

        group_by_alias: bool, optional, defaults to False
            If set to True, the result will be a dictionary with the rule alias as keys
                and a list of scraped data per alias as values.

        unique: bool, optional, defaults to True for non grouped results and
                False for grouped results.
            If set to True, will remove duplicates from returned result list.

        attr_fuzz_ratio: float in range [0, 1], optional, defaults to 1.0
            The fuzziness ratio threshold for matching html tag attributes.

        Returns:
        --------
        Pair of (similar, exact) results.
        See get_result_similar and get_result_exact methods.
        """
        pass

    def remove_rules(self, rules):
        """
        Removes a list of learned rules from stack_list.

        Parameters:
        ----------
        rules : list
            A list of rules to be removed

        Returns:
        --------
        None
        """
        pass

    def keep_rules(self, rules):
        """
        Removes all other rules except the specified ones.

        Parameters:
        ----------
        rules : list
            A list of rules to keep in stack_list and removing the rest.

        Returns:
        --------
        None
        """
        pass

    def set_rule_aliases(self, rule_aliases):
        """
        Sets the specified alias for each rule

        Parameters:
        ----------
        rule_aliases : dict
            A dictionary with keys of rule_id and values of alias

        Returns:
        --------
        None
        """
        pass

    def generate_python_code(self):
        # deprecated
        pass
