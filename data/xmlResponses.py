xml_data = {
    "employee" : '''<Employees>
                  <Employee>
                    <EmpId>001</EmpId>
                    <Name>Hindi News Bulletin | हिंदी समाचार बुलेटिन -01 April, 2020 (8 pm)</Name>
                    <Mobile>1-541-754-3010</Mobile>
                    <EmailId>steven@yourcomany.com</EmailId>
                  </Employee>
                  <Employee>
                    <EmpId>002</EmpId>
                    <Name>Mark</Name>
                    <Mobile>1-551-754-3010</Mobile>
                    <EmailId>mark@yourcomany.com</EmailId>
                  </Employee>
                  <Employee>
                    <EmpId>003</EmpId>
                    <Name>Adam</Name>
                    <Mobile>1-551-754-3010</Mobile>
                    <EmailId>mark@yourcomany.com</EmailId>
                  </Employee>
                </Employees>''',
    "data" : '''<?xml version="1.0"?>
                    <data>
                        <country name="Liechtenstein">
                            <rank>1</rank>
                            <year>2008</year>
                            <gdppc>141100</gdppc>
                        </country>
                        <country name="Singapore">
                            <rank>4</rank>
                            <year>2011</year>
                            <gdppc>59900</gdppc>
                        </country>
                        <country name="Panama">
                            <rank>68</rank>
                            <year>2011</year>
                            <gdppc>13600</gdppc>
                        </country>
                        <state name="Delhi">
                            <rank>68</rank>
                            <year>2011</year>
                            <gdppc>13600</gdppc>
                        </state>
                    </data>''',
                    "country2" : '''<?xml version="1.0"?>
                    <data>
                        <country name="Liechtenstein">
                            <rank>1</rank>
                            <year>2008</year>
                            <gdppc>141100</gdppc>
                            <neighbor name="Austria" direction="E"/>
                            <neighbor name="Switzerland" direction="W"/>
                        </country>
                        <country name="Singapore">
                            <rank>4</rank>
                            <year>2011</year>
                            <gdppc>59900</gdppc>
                            <neighbor name="Malaysia" direction="N"/>
                        </country>
                        <country name="Panama">
                            <rank>68</rank>
                            <year>2011</year>
                            <gdppc>13600</gdppc>
                            <neighbor name="Costa Rica" direction="W"/>
                            <neighbor name="Colombia" direction="E"/>
                        </country>
                        <state name="Delhi">
                            <rank>68</rank>
                            <year>2011</year>
                            <gdppc>13600</gdppc>
                            <neighbor name="Costa Rica" direction="W"/>
                            <neighbor name="Colombia" direction="E"/>
                        </state>
                    </data>''',
                    "Eaadhar" : '''<EaadharXamlSchema>
	<KycRes>
		<Rar>string</Rar>
		<UidData>
			<Poi>
				<dob>string</dob>
				<gender>string</gender>
				<name>string</name>
			</Poi>
			<Poa>
				<co>string</co>
				<country>string</country>
				<dist>string</dist>
				<lm>string</lm>
				<loc>string</loc>
				<pc>string</pc>
				<state>string</state>
				<vtc>string</vtc>
			</Poa>
			<LData>
				<co>string</co>
				<country>string</country>
				<dist>string</dist>
				<lang>string</lang>
				<lm>string</lm>
				<loc>string</loc>
				<name>string</name>
				<pc>string</pc>
				<state>string</state>
				<vtc>string</vtc>
			</LData>
			<Pht>string</Pht>
			<Prn>
				<type>string</type>
				<text>string</text>
			</Prn>
			<tkn>string</tkn>
			<uid>string</uid>
		</UidData>
		<Signature>
			<SignedInfo>
				<CanonicalizationMethod>
					<Algorithm>string</Algorithm>
				</CanonicalizationMethod>
				<SignatureMethod>
					<Algorithm>string</Algorithm>
				</SignatureMethod>
				<Reference>
					<Transforms>
						<Transform>
							<Algorithm>string</Algorithm>
						</Transform>
					</Transforms>
					<DigestMethod>
						<Algorithm>string</Algorithm>
					</DigestMethod>
					<DigestValue>string</DigestValue>
					<URI>string</URI>
				</Reference>
			</SignedInfo>
			<SignatureValue>string</SignatureValue>
			<KeyInfo>
				<X509Data>
					<X509SubjectName>string</X509SubjectName>
					<X509Certificate>string</X509Certificate>
				</X509Data>
			</KeyInfo>
			<xmlns>string</xmlns>
		</Signature>
		<code>string</code>
		<ret>string</ret>
		<ts>string</ts>
		<ttl>string</ttl>
		<txn>string</txn>
	</KycRes>
</EaadharXamlSchema>''',
        "XMLFormatSchema" : '''<XMLFormatSchema>
	<CertificateData>
	</CertificateData>
	<Signature>
		<SignedInfo>string</SignedInfo>
		<SignatureValue>string</SignatureValue>
		<KeyInfo>
			<X509Data>string</X509Data>
		</KeyInfo>
	</Signature>
</XMLFormatSchema>''',
"Envelope" : '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<SOAP-ENV:Body>
		<rpc:SubmitApplicationResponse xmlns:rpc="http://siebel.com/CustomUI">
			<FinalResponse>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48TGlzdE9mUGdTdHVkZW50TWFzdGVySW8KPjxIbHNEaXNlYXNlCj48RXJyb3JDb2RlCj48L0Vycm9yQ29kZQo+PEVycm9yTWVzc2FnZQo+U3R1ZGVudCBEYXRhIGlzIHNhdmVkIGFuZCBzdWJtaXR0ZWQuPC9FcnJvck1lc3NhZ2UKPjwvSGxzRGlzZWFzZQo+PC9MaXN0T2ZQZ1N0dWRlbnRNYXN0ZXJJbwo+</FinalResponse>
		</rpc:SubmitApplicationResponse>
	</SOAP-ENV:Body>
</SOAP-ENV:Envelope>''',
"employee2" : '''<Employees>
                  <Employee>
                    <EmpId>001</EmpId>
                    <Name>Steven</Name>
                    <Mobile>1-541-754-3010</Mobile>
                    <EmailId>steven@yourcomany.com</EmailId>
                  </Employee>
                  <Employee>
                    <EmpId>002</EmpId>
                    <Name>Mark</Name>
                    <Mobile>1-551-754-3010</Mobile>
                    <EmailId>mark@yourcomany.com</EmailId>
                  </Employee>
                  <Employee>
                    <EmpId>003</EmpId>
                    <Name>Adam</Name>
                    <Mobile>1-551-754-3010</Mobile>
                    <EmailId>mark@yourcomany.com</EmailId>
                  </Employee>
                  <country name="Liechtenstein">
                      <rank>1</rank>
                      <year>2008</year>
                      <gdppc>141100</gdppc>
                  </country>
                  <country name="Austria">
                      <rank>5</rank>
                      <year>2005</year>
                      <gdppc>141100</gdppc>
                  </country>
                </Employees>''',
                "Envelope" : '''<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<SOAP-ENV:Body>
		<rpc:SubmitApplicationResponse xmlns:rpc="http://siebel.com/CustomUI">
			<FinalResponse>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48TGlzdE9mUGdTdHVkZW50TWFzdGVySW8KPjxIbHNEaXNlYXNlCj48RXJyb3JDb2RlCj48L0Vycm9yQ29kZQo+PEVycm9yTWVzc2FnZQo+U3R1ZGVudCBEYXRhIGlzIHNhdmVkIGFuZCBzdWJtaXR0ZWQuPC9FcnJvck1lc3NhZ2UKPjwvSGxzRGlzZWFzZQo+PC9MaXN0T2ZQZ1N0dWRlbnRNYXN0ZXJJbwo+</FinalResponse>
		</rpc:SubmitApplicationResponse>
	</SOAP-ENV:Body>
</SOAP-ENV:Envelope>''',
"Book" : '''<"smp:book" xmlns:smp="http://example.com/schema">
xml:
    prefix: 'smp'
    namespace: 'http://example.com/schema'
</"smp:book">''',
"xml-book" : '''<book>
	<id>0</id>
	<xml-title>string</xml-title>
	<author>string</author>
</book>'''
}
