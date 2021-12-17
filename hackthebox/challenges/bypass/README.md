# Bypass
First you have to run this file on a window machine. When running the command `file Bypass.exe` you get the output `Bypass.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows`. Since this is a .NET file you you want download a decompiler for it. A good decompiler for it is IlSpy.


## method 0
```c#
// 0
using System;

public class 0
{
	public static string 0;

	public static string 1;

	public static string 2 = 5.8;

	public static void 0()
	{// this loops
		if (1())
		{
			2();
			return;
		}
		Console.WriteLine(5.0);
		0();
	}

	public static bool 1()
	{
		Console.Write(5.1); // asking for the username
		string text = Console.ReadLine(); // getting the user input
		Console.Write(5.2); // asking for the password
		string text2 = Console.ReadLine(); // getting the user password
		return false; // this always return false but change it so that it return true instead
	}

	public static void 2()
	{
		string text = 5.3;
		Console.Write(5.4); // change this to 5.3
		string text2 = Console.ReadLine(); // change this so that its 5.3, mscorlib.CommonLanguageRuntimeLibrary.System.Console.Readline()
		if (text == text2) // now that its true
		{
			Console.Write(5.5 + global::0.2 + 5.6);
			return;
		}
		Console.WriteLine(5.7);
		2();
	}
}

```


## new method 0
```c#
// 0
using System;

public class 0
{
	public static string 0;

	public static string 1;

	public static string 2 = 5.8;

	public static void 0()
	{
		if (1())
		{
			2();
			return;
		}
		Console.WriteLine(5.0);
		0();
	}

	public static bool 1()
	{
		Console.Write(5.1);
		string text = Console.ReadLine();
		Console.Write(5.2);
		string text2 = Console.ReadLine();
		return true;
	}

	public static void 2()
	{
		string text = 5.3;
		Console.Write(5.4);
		string text2 = 5.3;
		if (text == text2)
		{
			Console.Write(5.5 + global::0.2 + 5.6);
		}
		Console.WriteLine(5.7);
		2();
	}
}


```

## flag

`HTB{SuP3rC00lFL4g}`