$user = @{
    Name = "John"
    Role = "Admin"
}
$user.ContainsKey("Role")
$user.Add("Age", 30)
$user.Remove("Role")