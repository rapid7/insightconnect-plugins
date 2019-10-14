param (
    [string]$Username,
    [string]$Password,
    [string]$Sender,
    [string]$StartDate, 
    [string]$EndDate, 
    [string]$Office365URI = "https://outlook.office365.com/powershell-liveid/"
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

if ($StartDate.Length -eq 0) {
    throw "Start Date is required"
}

if ($EndDate.Length -eq 0) {
    throw "End Date is required"
}

if ($Sender.Length -eq 0) {
    throw "Sender is required"
}

$timeout = New-TimeSpan -Minutes $TimeoutInMinutes
$stopwatch = [diagnostics.stopwatch]::StartNew()

$Credentials = New-Object System.Management.Automation.PSCredential($Username, $SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

Import-PSSession $Session -DisableNameChecking

$result = Get-MessageTrace -SenderAddress $Sender -StartDate $StartDate -EndDate $EndDate | Select-Object -Property * | ConvertTo-Json -AsArray

Write-Host ($result)
Remove-PSSession $Session