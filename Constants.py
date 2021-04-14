EVT_SEARCH_STARTED = 0
EVT_SEARCH_SUCCESS = 1
EVT_SEARCH_FAILURE = 2
EVT_CLOSE_OUTPUT_PAGE = 3
EVT_TERMINATE_THREAD = 4

SERVER_RESPONSE_UPLOAD_FAILURE = b'0'
SERVER_RESPONSE_UPLOAD_SUCCESS = b'1'
SERVER_RESPONSE_QUERY_FAILURE = b'2'
SERVER_RESPONSE_QUERY_SUCCESS = b'3'

REQUEST_TYPE_UPLOAD = b'0'
REQUEST_TYPE_QUERY = b'1'

COLLECTION_SAMPLE = u'kwic_collection'
DOCUMENT_QUERY_URLS = u'kwic_query_document'
ARG_KWIC_KEYWORD_DATA = u'kwicKeywordData'
ARG_URL_ORIGINAL_KEYWORDS = u'urlOriginalKeywords'
ARG_URL = u'url'
ARG_NOISE_WORDS = u'noiseWords'
ARG_KEYWORDS = u'keywords'