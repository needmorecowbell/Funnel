rule personal_info 
{

	meta:
		Author = "Adam Musciano"
		Category = "personal"
                Description = "This rule detects any personal info found in an article"

	strings:
		
		$m1 = "<Full name>"" nocase ascii
		$m2 = "<email>" nocase ascii
		$m3 = "<website>" nocase ascii
                $m4 = "<username>" nocase ascii
                $m5 = "<server ip address>" ascii
                $m6 = "<phone number>" nocase ascii
                $m7 = "<address>" nocase ascii
	condition:
	       any of them 
		
}
