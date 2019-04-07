rule contains_elon_musk 
{

	meta:
		Author = "Adam Musciano"
		Category = "personal"
                Description = "This rule detects any mention of elon_musk info found in an article"

	strings:
		
		$m1 = "Elon Musk" nocase ascii

		$m2 = "Elon" fullword ascii
		$m3 = "Musk" fullword ascii
	condition:
	        $m1 or ($m2 and $m3) 
		
}
