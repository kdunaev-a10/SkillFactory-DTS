$search = New-Object DirectoryServices.DirectorySearcher([ADSI]"")
$search.filter = "(servicePrincipalName=*)"
$results = $search.Findall()
foreach($result in $results) {
    $userEntry = $result.GetDirectoryEntry()
    Write-Host "Object-Name = " $userEntry.name -BackgroundColor "yellow" -ForegroundColor "black"
    Write-Host "DN      =     " $userEntry.distinguishedName
    Write-Host "Object Cat. = " $userEntry.objectCategory
    Write-Host "servicePrincipalNames"
    $i=1
    foreach($SPN in $userEntry.servicePrincipalName) {
        Write-Host "SPN(" $i ")    =    " $SPN
        $i+=1
    }
    Write-Host ""
}

#Get-ADComputer -Filter * -Properties * | FT name, ipv4Address
 