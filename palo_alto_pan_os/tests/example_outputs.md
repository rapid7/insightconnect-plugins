# Example outputs

This document contains raw example outputs from PAN-OS.
The purpose of these outputs is to help developers understand expected outputs from PAN-OS.

## Get security policy

### Active policy

`<response status="success" code="19"><result total-count="1" count="1">
  <entry name="newrule">
    <to>
      <member>any</member>
    </to>
    <from>
      <member>any</member>
    </from>
    <source>
      <member>10.4.88.244</member>
    </source>
    <destination>
      <member>10.10.10.10</member>
      <member>10.4.88.244</member>
    </destination>
    <service>
      <member>any</member>
    </service>
    <application>
      <member>any</member>
    </application>
    <category>
      <member>any</member>
    </category>
    <hip-profiles>
      <member>any</member>
    </hip-profiles>
    <source-user>
      <member>any</member>
    </source-user>
    <action>deny</action>
  </entry>
</result></response>`

### Candidate

`<response status="success" code="19"><result total-count="1" count="1">
  <entry name="newrule" admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
    <to admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">test</member>
    </to>
    <from admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">any</member>
    </from>
    <source admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">10.4.88.244</member>
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">192.168.1.3</member>
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">192.168.1.10</member>
    </source>
    <destination admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">10.10.10.10</member>
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">10.4.88.244</member>
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">192.168.1.3</member>
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">192.168.1.10</member>
    </destination>
    <service admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">any</member>
    </service>
    <application admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">any</member>
    </application>
    <category admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">any</member>
    </category>
    <hip-profiles admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">any</member>
    </hip-profiles>
    <source-user admin="admin" dirtyId="62" time="2019/03/01 09:07:00">
      <member admin="admin" dirtyId="62" time="2019/03/01 09:07:00">bob</member>
    </source-user>
    <action admin="admin" dirtyId="62" time="2019/03/01 09:07:00">deny</action>
  </entry>
</result></response>`