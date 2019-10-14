param (
    [string]$Username = "",
    [string]$Password = "",
    [string]$EmailOrDomainToBlock = "somereallysuperfake@emailgarbage.com",
    [string]$RuleName = "InsightConnect Block List"
)

$Office365URI = "https://outlook.office365.com/powershell-liveid/"

if($Username.Length -eq 0){
    throw "Username is required."
}

if($Password.Length -eq 0){
    throw "Password is required."
}
else{
    $SecPassword = ConvertTo-SecureString $Password -AsPlainText -Force
}

$Credentials = New-Object System.Management.Automation.PSCredential($Username,$SecPassword)
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $Office365URI -Credential $Credentials -Authentication Basic -AllowRedirection

Write-Host "Attempting to block: $($EmailOrDomainToBlock)"
Write-Host "In Transport Rule: $($RuleName)"

Import-PSSession $Session -DisableNameChecking

$CurrentList = Get-TransportRule $RuleName -ErrorAction SilentlyContinue | Select-Object -ExpandProperty "FromAddressContainsWords" -ErrorAction SilentlyContinue

if ($null -ne $CurrentList){
    Write-Host "Found rule $($RuleName)"
    [System.Collections.ArrayList]$BlockList = $CurrentList.split(",")

    if($BlockList.Contains($EmailOrDomainToBlock)){
        Write-Host "Blocklist already contains $($EmailOrDomainToBlock)"
        Remove-PSSession $Session
        Exit
    }

    Write-Host "Adding $($EmailOrDomainToBlock) to transport rule named $($RuleName)"
    $Blocklist.Add($EmailOrDomainToBlock)

    # Verify our list isn't too big. 
    $BlockListString = -join $BlockList    
    $Length = $BlockListString.Length
    Write-Host "Blocklist length in characters: $($Length)"
    while($Length -gt 8100){ # Max length of a command is 8192 - Giving myself some padding
        $Length = 0 
        $BlockList.RemoveAt(0) # Making the assumption that the list maintains its order
        $BlockListString = -join $BlockList
        $Length = $BlockListString.Length
    }
    Write-Host "BlockList characters length: $($Length)"

    Write-Host "New blocklist follows: "
    Write-Host $BlockList

    Set-TransportRule $RuleName -FromAddressContainsWords $BlockList
}
else {
    Write-Host "Creating rule $($RuleName)"
    New-TransportRule -Name $RuleName -Comments $RuleName -Priority '0' -Enabled $true -FromAddressContainsWords $EmailOrDomainToBlock -DeleteMessage $true
}

Write-Host "Blocking finished"
Remove-PSSession $Session
