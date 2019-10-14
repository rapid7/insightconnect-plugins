<#
.SYNOPSIS
    This script executes the mass delete functionality of the Office 365 Security and Compliance application. The script makes use of the Policy and Compliance Content Search actions exposed by Office 365. More information is available here:
    https://docs.microsoft.com/en-us/powershell/module/exchange/policy-and-compliance-content-search/new-compliancesearchaction?view=exchange-ps

.DESCRIPTION
    The Mass-Delete script finds all the e-mails in your organization based on the search criteria you give it and deletes them.

    The known limitations of this script are a maximum of 10 items per mailbox and a limit of 50,000 mailboxes in an organization. For help with large organizations follow this link: https://docs.microsoft.com/en-us/office365/securitycompliance/search-for-and-delete-messages-in-your-organization

    Un-indexed items cannot be removed from mailboxes using this script.

.PARAMETER Username
	Username with administrative rights to Office 365

.PARAMETER Password
	Securestring password

.PARAMETER ComplianceSearchName
	The name of the compliance search used to find content to delete

.PARAMETER ContentMatchQuery
	This parameter uses a text search string or a query that's formatted by using the Keyword Query Language (KQL). For more information about KQL, see Keyword Query Language syntax reference (https://go.microsoft.com/fwlink/p/?linkid=269603).

.PARAMETER TimeoutInMinutes
	OPTIONAL: Default 60: The length in minutes after which the script terminates. The timeout resets after a successful search and is applied again to the delete action. 

.PARAMETER DeleteItems
	OPTIONAL: Default $false: The script only executes the delete action if this parameter is $true.  The default value of $false allows configuration debugging without accidentally deleting content. 

.PARAMETER Office365URI
	OPTIONAL: Default https://ps.compliance.protection.outlook.com/powershell-liveid/: This parameter sets the location of the Office 365 or on-premise exchange server from which to execute the compliance actions. 

.EXAMPLE
    Mass-Delete -Username someuser@microsoft.com -Password password -ComplianceSearchName "Content Search" -ContentMatchQuery subject:"Phishy"

.LINK
    https://www.rapid7.com/
#>

param (
    [string]$Username,
    [string]$Password,
    [string]$ComplianceSearchName,
    [string]$ContentMatchQuery,
    [Int32]$TimeoutInMinutes = 60, 
    [string]$DeleteItems = $false,
    [string]$Office365URI = "https://ps.compliance.protection.outlook.com/powershell-liveid/"
)

if($Username.Length -eq 0){
    throw "Username is required."
}

if($Password.Length -eq 0){
    throw "Password is required."
}
else{
    $SecPassword = ConvertTo-SecureString $Password -AsPlainText -Force
}

if($ComplianceSearchName.Length -eq 0){
    throw "ComplianceSearchName is required"
}

if($ContentMatchQuery.Length -eq 0){
    throw "ContentMatchQuery is required. For more information go to https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference."
}

$DeleteItems = [boolean]$DeleteItems

$timeout = New-TimeSpan -Minutes $TimeoutInMinutes
$stopwatch = [diagnostics.stopwatch]::StartNew()

$Credentials = New-Object System.Management.Automation.PSCredential($Username,$SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

Import-PSSession $Session -DisableNameChecking -ErrorAction SilentlyContinue

#This is handy for debugging. Remove this for production use.
#Remove-ComplianceSearch -Identity $ComplianceSearchName -Confirm:$false

New-ComplianceSearch -Name $ComplianceSearchName -ExchangeLocation 'All' -AllowNotFoundExchangeLocationsEnabled $true -ContentMatchQuery $ContentMatchQuery -ErrorAction SilentlyContinue

Write-Host -NoNewline "Creating Search."
Start-ComplianceSearch -Identity $ComplianceSearchName -Force

Write-Output " "
Write-Host -NoNewline "Running Search..."

$result = Get-ComplianceSearch -Identity $ComplianceSearchName

if($null -ne $result){
    while($result.status -ne "Completed"){
        Write-Host -NoNewline "."
        $result = Get-ComplianceSearch -Identity $ComplianceSearchName
        
        if($stopwatch.elapsed -gt $timeout){
            Remove-PSSession $Session
            throw "Timeout was exceeded."
        }
        Start-Sleep -Seconds 10       
    }
}

Write-Output "Search Completed."
Write-Output "Resetting timeout, attempting to delete."
$timeout = New-TimeSpan -Minutes $TimeoutInMinutes
$stopwatch = [diagnostics.stopwatch]::StartNew()

if($DeleteItems){
    Write-Host -NoNewline "Deleting..."
    $deleteResult = New-ComplianceSearchAction -SearchName $ComplianceSearchName -Purge -PurgeType SoftDelete -Confirm:$false

    if($null -ne $deleteResult){
        while($result.status -ne "Completed"){
            Write-Host -NoNewline "."
            $result = Get-ComplianceSearch -Identity $ComplianceSearchName

            if($stopwatch.elapsed -gt $timeout){
                Remove-PSSession $Session                
                throw "Timeout was exceeded."
            }

            Start-Sleep -Seconds 10
        }
    }
}
else{
    Write-Host "DeleteItems was set to false. Delete step was skipped."
}

Remove-PSSession $Session
