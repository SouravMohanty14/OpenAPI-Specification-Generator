xml_data = {
    "employee" : '''<Employees>
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
    "country" : '''<?xml version="1.0"?>
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
                    </data>'''
}
