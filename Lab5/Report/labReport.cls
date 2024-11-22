\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{labReport}[Format class for CSC2621 lab reports]

\LoadClass[12pt]{article}

% Formatting packages
\RequirePackage[table,xcdraw]{xcolor}
\RequirePackage[letterpaper,margin=1in,tmargin=0.5in,includeheadfoot]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[labelfont=bf]{caption}
\RequirePackage{enumitem, fourier, graphicx, float, fancyhdr, titlesec, calc, booktabs, multicol, multirow, blindtext, siunitx, tabularx, listings, tablefootnote}

% Hyperlinks and colors
\RequirePackage[colorlinks=true,linkcolor=blue, filecolor=magenta, urlcolor=blue]{hyperref}


% Page setup
\setkeys{Gin}{width=\textwidth}
\setlength\parskip{1em plus 0.1em minus 0.2em}

% Title and section formatting
\titleformat{\section}{\bfseries\fontsize{16pt}{12}\selectfont}{}{0em}{}
\titlespacing\section{0pt}{18pt plus 2pt minus 2pt}{0pt plus 2pt minus 2pt}

\titleformat{\subsection}{\bfseries\fontsize{12pt}{12}\selectfont}{}{0em}{}
\titlespacing\subsection{0pt}{0pt plus 2pt minus 2pt}{0pt plus 2pt minus 2pt}

% Figure and table placement
\makeatletter
\setlist{topsep=0pt, itemsep=3pt, parsep=2pt}
\renewcommand*{\fps@figure}{H}
\renewcommand*{\fps@table}{H}
\g@addto@macro\@floatboxreset\centering

\newcommand{\submissionDate}[1]{\def\submissionDate{#1}}
\newcommand{\laboratoryDate}[1]{\def\laboratoryDate{#1}}
\newcommand{\prof}[1]{\def\prof{#1}}
\newcommand{\className}[1]{\def\className{#1}}
\newcommand{\classCode}[1]{\def\classCode{#1}}
\newcommand{\semester}[1]{\def\semester{#1}}
\newcommand{\labWeek}[1]{\def\labWeek{#1}}

\fancypagestyle{firststyle}
{
    \fancyhf{}
    
    \lhead{
        \includegraphics[height=36pt, width=29pt]{msoe.png}
        \Large{
            \classCode - \className \\
            Lab Week \#\labWeek \\
            \submissionDate{}
        }
    }
    
    \rhead{
        \Large{
            \prof \\
            \@author \\
            \laboratoryDate
        }
    }
    \cfoot{1}

    \newgeometry{margin=1in,tmargin=.5in,headsep=1.25in,includehead}
    
}

\renewcommand\maketitle{
{
\thispagestyle{firststyle}
\begin{center}
    \LARGE{\@title}
\end{center}
}

}
\makeatother
