# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.datagen.translation.en
   :platform: Unix
   :synopsis: English language translation for Datagen extension
.. moduleauthor:: Petr Czaderna <pc@hydratk.org>

"""

language = {
    'name': 'English',
    'ISO-639-1': 'en'
}

msg = {
    'datagen_received_cmd': ["Received command: '{0}'"],
    'datagen_missing_option': ["Missing option: {0}"],
    'datagen_invalid_option_value': ["Invalid option {0} value, supported values: {1}"],
    'datagen_action_error': ["Error within action {0}"],
    'datagen_file_not_found': ["File {0} not found"],
    'datagen_asn1_compile': ["Compiling ASN.1 specification: '{0}'"],
    'datagen_asn1_compiled': ["ASN.1 specification compiled"],
    'datagen_asn1_decode': ["Decoding input file: '{0}' from format: '{1}' according to element: '{2}' in specification: '{3}'"],
    'datagen_asn1_decoded': ["Decoded to output file: '{0}'"],
    'datagen_asn1_encode': ["Encoding input file: '{0}' to format: '{1}' according to element: '{2}' in specification: '{3}'"],
    'datagen_asn1_encoded': ["Encoded to output file: '{0}'"],
    'datagen_asn1_transcode': ["Transcoding input file: '{0}' from format: '{1}' to format: '{2}' according to element: '{3}' specification: '{4}'"],
    'datagen_asn1_transcoded': ["Transcoded to output file: '{0}'"],
    'datagen_jsongen_import_spec': ["Importing JSON specification: '{0}'"],
    'datagen_jsongen_spec_imported': ["JSON specification imported"],
    'datagen_jsongen_spec_not_imported': ["JSON specification not imported"],
    'datagen_jsongen_write_sample': ["Creating sample JSON document"],
    'datagen_jsongen_sample_written': ["Sample written to file: '{0}'"],
    'datagen_xmlgen_import_spec': ["Importing XML specification: '{0}'"],
    'datagen_xmlgen_spec_imported': ["XML specification imported"],
    'datagen_xmlgen_spec_not_imported': ["XML specification not imported"],
    'datagen_xmlgen_unknown_spec': ["Unknown specification type: {0}"],
    'datagen_xmlgen_invalid_spec': ["Invalid XML specification: {0}"],
    'datagen_xmlgen_write_sample': ["Creating sample XML document"],
    'datagen_xmlgen_sample_written': ["Sample written to file: '{0}'"],
    'datagen_adapter_parsing_suite': ["Parsing suite file: '{0}'"],
    'datagen_adapter_suite_parsed': ["Suite successfully parsed"],
    'datagen_adapter_parsing_test': ["Parsing test"],
    'datagen_adapter_test_parsed': ["Test successfully parsed"],
    'datagen_adapter_cmd_unknown': ["Detected unknown command '{0}'"],
    'datagen_adapter_cmd_dummy': ["Detected not supported command '{0}'"],
    'datagen_adapter_script_adapted': ["Script adapted"]
}
