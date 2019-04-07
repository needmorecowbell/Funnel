rule contains_tacos 
{

	meta:
		Author = "Adam Musciano"
		Category = "Cooking"
                Description = "This rule detects content that contains tacos"

	strings:
		
		$s1 = "tacos" fullword nocase ascii

		$m2 = "taco" fullword nocase ascii

	condition:
	        any of them	
		
}
