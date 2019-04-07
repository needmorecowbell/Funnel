rule contains_trump 
{

	meta:
		Author = "Adam Musciano"
		Category = "personal"
                Description = "This rule detects any mention of trump info found in an article"

	strings:
		
		$m1 = "Donald Trump" nocase ascii
		$m2 = "Trump" fullword ascii
	condition:
	        any of them 
		
}
