# revision 18651
# category Package
# catalog-ctan /fonts/cyklop
# catalog-date 2008-12-15 08:58:20 +0100
# catalog-license gfl
# catalog-version 0.915
Name:		texlive-cyklop
Version:	0.915
Release:	2
Summary:	The Cyclop typeface
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cyklop
License:	GFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyklop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyklop.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Cyclop typeface was designed in the 1920s at the workshop
of Warsaw type foundry "Odlewnia Czcionek J. Idzkowski i S-ka".
This sans serif typeface has a highly modulated stroke so it
has high typographic contrast. The vertical stems are much
heavier then horizontal ones. Most characters have thin
rectangles as additional counters giving the unique shape of
the characters. The lead types of Cyclop typeface were produced
in slanted variant at sizes 8-48 pt. It was heavily used for
heads in newspapers and accidents prints. Typesetters used
Cyclop in the inter-war period, during the occupation in the
underground press. The typeface was used until the beginnings
of the offset print and computer typesetting era. Nowadays it
is hard to find the metal types of this typeface. The font was
generated using the Metatype1 package. Then the original set of
characters was completed by adding the full set of accented
letters and characters of the modern Latin alphabets (including
Vietnamese). The upright variant was generated and it was more
complicated task than it appeared at the beginning. 11 upright
letters of the Cyclop typeface were presented in the book by
Filip Trzaska, "Podstawy techniki wydawniczej" ("Foundation of
the publishing techonology"), Warsaw 1967. But even the author
of the book does not know what was the source of the presented
examples. The fonts are distributed in the Type1 and OpenType
formats along with the files necessary for use these fonts in
TeX and LaTeX including encoding definition files: T1 (ec), T5
(Vietnamese), OT4, QX, texnansi and nonstandard ones (IL2 for
Czech fonts).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/cyklop/cyklopi.afm
%{_texmfdistdir}/fonts/afm/public/cyklop/cyklopr.afm
%{_texmfdistdir}/fonts/enc/dvips/cyklop/cs-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/cs-cyklop.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/ec-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/ec-cyklop.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/l7x-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/l7x-cyklop.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/ly1-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/ly1-cyklop.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/qx-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/qx-cyklop.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/t5-cyklop-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/cyklop/t5-cyklop.enc
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-cs.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-ec.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-l7x.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-ly1.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-qx.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop-t5.map
%{_texmfdistdir}/fonts/map/dvips/cyklop/cyklop.map
%{_texmfdistdir}/fonts/opentype/public/cyklop/cyklop-italic.otf
%{_texmfdistdir}/fonts/opentype/public/cyklop/cyklop-regular.otf
%{_texmfdistdir}/fonts/tfm/public/cyklop/cs-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/cs-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/cs-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/cs-cyklopr.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ec-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ec-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ec-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ec-cyklopr.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/l7x-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/l7x-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/l7x-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/l7x-cyklopr.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ly1-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ly1-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ly1-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/ly1-cyklopr.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/qx-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/qx-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/qx-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/qx-cyklopr.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/t5-cyklopi-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/t5-cyklopi.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/t5-cyklopr-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/cyklop/t5-cyklopr.tfm
%{_texmfdistdir}/fonts/type1/public/cyklop/cyklopi.pfb
%{_texmfdistdir}/fonts/type1/public/cyklop/cyklopr.pfb
%{_texmfdistdir}/tex/latex/cyklop/cyklop.sty
%{_texmfdistdir}/tex/latex/cyklop/il2cyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/l7xcyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/ly1cyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/ot1cyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/ot4cyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/qxcyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/t1cyklop.fd
%{_texmfdistdir}/tex/latex/cyklop/t5cyklop.fd
%doc %{_texmfdistdir}/doc/fonts/cyklop/00readme
%doc %{_texmfdistdir}/doc/fonts/cyklop/00readme-pl
%doc %{_texmfdistdir}/doc/fonts/cyklop/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/cyklop/MANIFEST.txt
%doc %{_texmfdistdir}/doc/fonts/cyklop/cyklop-info.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.915-2
+ Revision: 750759
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.915-1
+ Revision: 718196
- texlive-cyklop
- texlive-cyklop
- texlive-cyklop
- texlive-cyklop

