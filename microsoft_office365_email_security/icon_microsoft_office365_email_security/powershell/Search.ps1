param (
    [string]$Username,
    [string]$Password,
    [string]$ComplianceSearchName,
    [string]$ContentMatchQuery,
    [Int32]$TimeoutInMinutes = 60,
    [string]$Office365URI = "https://ps.compliance.protection.outlook.com/powershell-liveid/"
)

if ($Username.Length -eq 0) {
    throw "Username is required."
}

if ($Password.Length -eq 0) {
    throw "Password is required."
}
else {
    $SecPassword = ConvertTo-SecureString $Password -AsPlainText -Force
}

if ($ComplianceSearchName.Length -eq 0) {
    throw "ComplianceSearchName is required"
}

if ($ContentMatchQuery.Length -eq 0) {
    throw "ContentMatchQuery is required. For more information go to https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference."
}

$timeout = New-TimeSpan -Minutes $TimeoutInMinutes
$stopwatch = [diagnostics.stopwatch]::StartNew()

$Credentials = New-Object System.Management.Automation.PSCredential($Username, $SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

Import-PSSession $Session -DisableNameChecking -ErrorAction SilentlyContinue

#This is handy for debugging. Remove this for production use.
#Remove-ComplianceSearch -Identity $ComplianceSearchName -Confirm:$false

New-ComplianceSearch -Name $ComplianceSearchName -ExchangeLocation 'All' -AllowNotFoundExchangeLocationsEnabled $true -ContentMatchQuery $ContentMatchQuery -ErrorAction SilentlyContinue | Out-Null

Write-Host -NoNewline "Creating Search."
Start-ComplianceSearch -Identity $ComplianceSearchName -Force

Write-Output " "
Write-Host -NoNewline "Running Search..."

$result = Get-ComplianceSearch -Identity $ComplianceSearchName

if ($null -ne $result) {
    while ($result.status -ne "Completed") {
        Write-Host -NoNewline "."
        $result = Get-ComplianceSearch -Identity $ComplianceSearchName
        
        if ($stopwatch.elapsed -gt $timeout) {
            Remove-PSSession $Session
            throw "Timeout was exceeded."
        }
        Start-Sleep -Seconds 10       
    }
}

Remove-PSSession $Session

Write-Host ($result | Select-Object -Property "SearchStatistics")