# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tdsfrmath
# catalog-date 2009-06-22 16:39:08 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-tdsfrmath
Version:	1.3
Release:	4
Summary:	Macros for French teachers of mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tdsfrmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of macros for French maths teachers in colleges
and lycees (and perhaps elsewhere). It is hoped that the
package will facilitate the everyday use of LaTeX by
mathematics teachers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tdsfrmath/suite.sto
%{_texmfdistdir}/tex/latex/tdsfrmath/taupe.sto
%{_texmfdistdir}/tex/latex/tdsfrmath/tdsfrmath.sty
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/LISEZMOI
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/README
%doc %{_texmfdistdir}/doc/latex/tdsfrmath/tdsfrmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tdsfrmath/Makefile
%doc %{_texmfdistdir}/source/latex/tdsfrmath/tdsfrmath.dtx
%doc %{_texmfdistdir}/source/latex/tdsfrmath/tdsfrmath.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 756549
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719662
- texlive-tdsfrmath
- texlive-tdsfrmath
- texlive-tdsfrmath

