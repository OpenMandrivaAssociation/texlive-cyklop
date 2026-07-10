%global tl_name cyklop
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.915
Release:	%{tl_revision}.1
Summary:	The Cyclop typeface
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cyklop
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyklop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyklop.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Cyclop typeface was designed in the 1920s at the workshop of Warsaw
type foundry "Odlewnia Czcionek J. Idzkowski i S-ka". This sans serif
typeface has a highly modulated stroke so it has high typographic
contrast. The vertical stems are much heavier then horizontal ones. Most
characters have thin rectangles as additional counters giving the unique
shape of the characters. The lead types of Cyclop typeface were produced
in slanted variant at sizes 8-48 pt. It was heavily used for heads in
newspapers and accidents prints. Typesetters used Cyclop in the inter-
war period, during the occupation in the underground press. The typeface
was used until the beginnings of the offset print and computer
typesetting era. Nowadays it is hard to find the metal types of this
typeface. The font was generated using the Metatype1 package. Then the
original set of characters was completed by adding the full set of
accented letters and characters of the modern Latin alphabets (including
Vietnamese). The upright variant was generated and it was more
complicated task than it appeared at the beginning. 11 upright letters
of the Cyclop typeface were presented in the book by Filip Trzaska,
"Podstawy techniki wydawniczej" ("Foundation of the publishing
technology"), Warsaw 1967. But even the author of the book does not know
what was the source of the presented examples. The fonts are distributed
in the Type1 and OpenType formats along with the files necessary for use
these fonts in TeX and LaTeX including encoding definition files: T1
(ec), T5 (Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for
Czech fonts).

