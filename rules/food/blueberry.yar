rule Blueberry_baked_recipe 
{

	meta:
		Author = "Adam Musciano"
		Category = "Cooking"
                Description = "This rule detects content that contains baked goods with blueberries"

	strings:
		
		$s1 = "blueberry" nocase ascii

		$m2 = "muffin" nocase ascii
		$m3 = "pancake" nocase ascii
                $m4 = "cupcake" nocase ascii
                $m5 = "cake" nocase ascii
                $m6 = "cookie" nocase ascii
                $m7 = "pastry" nocase ascii
                $m8 = "scone" nocase ascii

	condition:
	        $s1 and (1 of ($m*) )	
		
}
