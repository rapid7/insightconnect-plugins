param (
    [string]$Username,
    [string]$Password,
    [string]$ComplianceSearchName,
    [Int32]$TimeoutInMinutes = 60, 
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

$timeout = New-TimeSpan -Minutes $TimeoutInMinutes  

$Credentials = New-Object System.Management.Automation.PSCredential($Username,$SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

Import-PSSession $Session -DisableNameChecking -ErrorAction SilentlyContinue

$stopwatch = [diagnostics.stopwatch]::StartNew()

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

Remove-PSSession $Session