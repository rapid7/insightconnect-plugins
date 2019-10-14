param (
    [string]$Username,
    [string]$Password
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

$Office365URI = "https://outlook.office365.com/powershell-liveid/"

$Credentials = New-Object System.Management.Automation.PSCredential($Username,$SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

$Success = $false

if($null -ne $Session){
    $Success = $true
}

Remove-PSSession $Session

Write-Host $Success


