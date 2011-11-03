# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tdsfrmath
# catalog-date 2009-06-22 16:39:08 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-tdsfrmath
Version:	1.3
Release:	1
Summary:	Macros for French teachers of mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tdsfrmath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tdsfrmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A collection of macros for French maths teachers in colleges
and lycees (and perhaps elsewhere). It is hoped that the
package will facilitate the everyday use of LaTeX by
mathematics teachers.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
