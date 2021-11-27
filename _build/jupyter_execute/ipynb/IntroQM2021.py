#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-Quantum-Mechanics" data-toc-modified-id="Introduction-to-Quantum-Mechanics-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to Quantum Mechanics</a></span><ul class="toc-item"><li><span><a href="#🎯-Objective¶" data-toc-modified-id="🎯-Objective¶-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>🎯 Objective¶</a></span></li><li><span><a href="#📜-Instructions" data-toc-modified-id="📜-Instructions-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>📜 Instructions</a></span></li><li><span><a href="#Wave-Particle-Duality" data-toc-modified-id="Wave-Particle-Duality-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Wave-Particle Duality</a></span><ul class="toc-item"><li><span><a href="#🎲-Particle-like-features-of-light." data-toc-modified-id="🎲-Particle-like-features-of-light.-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>🎲 Particle-like features of light.</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🪙-Properties-of-photons" data-toc-modified-id="🪙-Properties-of-photons-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>🪙 Properties of photons</a></span></li><li><span><a href="#🪙-Properties-of-photons" data-toc-modified-id="🪙-Properties-of-photons-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>🪙 Properties of photons</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.5"><span class="toc-item-num">1.3.5&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🎲-Properties-of-photons" data-toc-modified-id="🎲-Properties-of-photons-1.3.6"><span class="toc-item-num">1.3.6&nbsp;&nbsp;</span>🎲 Properties of photons</a></span></li><li><span><a href="#🖩-Momentum-from-a-green-laser-pointer" data-toc-modified-id="🖩-Momentum-from-a-green-laser-pointer-1.3.7"><span class="toc-item-num">1.3.7&nbsp;&nbsp;</span>🖩 Momentum from a green laser pointer</a></span></li><li><span><a href="#🖩-Wavelength-emitted-by-a-radiopharmaceutical" data-toc-modified-id="🖩-Wavelength-emitted-by-a-radiopharmaceutical-1.3.8"><span class="toc-item-num">1.3.8&nbsp;&nbsp;</span>🖩 Wavelength emitted by a radiopharmaceutical</a></span></li><li><span><a href="#🪙-Davisson-Germer-experiment" data-toc-modified-id="🪙-Davisson-Germer-experiment-1.3.9"><span class="toc-item-num">1.3.9&nbsp;&nbsp;</span>🪙 Davisson-Germer experiment</a></span></li><li><span><a href="#🎲-Davisson-Germer-experiment" data-toc-modified-id="🎲-Davisson-Germer-experiment-1.3.10"><span class="toc-item-num">1.3.10&nbsp;&nbsp;</span>🎲 Davisson-Germer experiment</a></span></li><li><span><a href="#🖩-Rydberg's-Law" data-toc-modified-id="🖩-Rydberg's-Law-1.3.11"><span class="toc-item-num">1.3.11&nbsp;&nbsp;</span>🖩 Rydberg's Law</a></span></li><li><span><a href="#🎲-Wave-properties-of-particles" data-toc-modified-id="🎲-Wave-properties-of-particles-1.3.12"><span class="toc-item-num">1.3.12&nbsp;&nbsp;</span>🎲 Wave properties of particles</a></span></li><li><span><a href="#🎲-Particle-properties-of-waves" data-toc-modified-id="🎲-Particle-properties-of-waves-1.3.13"><span class="toc-item-num">1.3.13&nbsp;&nbsp;</span>🎲 Particle properties of waves</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.14"><span class="toc-item-num">1.3.14&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🖩-De-Broglie-wavelength-of-a-baseball" data-toc-modified-id="🖩-De-Broglie-wavelength-of-a-baseball-1.3.15"><span class="toc-item-num">1.3.15&nbsp;&nbsp;</span>🖩 De Broglie wavelength of a baseball</a></span></li></ul></li><li><span><a href="#The-Schrödinger-Equation" data-toc-modified-id="The-Schrödinger-Equation-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>The Schrödinger Equation</a></span><ul class="toc-item"><li><span><a href="#✍️-Time-Dependent-Schrödinger-Equation" data-toc-modified-id="✍️-Time-Dependent-Schrödinger-Equation-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>✍️ Time-Dependent Schrödinger Equation</a></span></li><li><span><a href="#🎲-Hamiltonian-operator" data-toc-modified-id="🎲-Hamiltonian-operator-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>🎲 Hamiltonian operator</a></span></li></ul></li><li><span><a href="#Mathematics" data-toc-modified-id="Mathematics-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Mathematics</a></span><ul class="toc-item"><li><span><a href="#🪙-Mathematical-Properties-of-the-wavefunction" data-toc-modified-id="🪙-Mathematical-Properties-of-the-wavefunction-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>🪙 Mathematical Properties of the wavefunction</a></span></li><li><span><a href="#🎲-Complex-Conjugation" data-toc-modified-id="🎲-Complex-Conjugation-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>🎲 Complex Conjugation</a></span></li><li><span><a href="#✍️-Complex-Conjugation" data-toc-modified-id="✍️-Complex-Conjugation-1.5.3"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>✍️ Complex Conjugation</a></span></li><li><span><a href="#🪙-Eigenfunctions-of-the-kinetic-energy-operator" data-toc-modified-id="🪙-Eigenfunctions-of-the-kinetic-energy-operator-1.5.4"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>🪙 Eigenfunctions of the kinetic-energy operator</a></span></li></ul></li></ul></li></ul></div>

# # Introduction to Quantum Mechanics
# 
# ##  &#x1f3af; Objective¶
# To review basic aspects of quantum mechanics.
# 
# ## &#x1f4dc; Instructions
# Before you turn this problem in, make sure everything runs as expected. First, restart the kernel (in the menubar, select Kernel → Restart) and then run all cells (in the menubar, select Cell → Run All).
# 
# Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE", as well as your name, username (the prefix to your @university.ext e-mail), and student ID number in the cell below

# > **Note**: You should remove "not implemented errors" after you complete your work on the solutions.

# In[1]:


Name = "First M. Last"
email_user_name = "username"
ID_number = 1234567

# It's useful to import these libraries. 
# You can import others or not even use these, though.
import numpy as np
import scipy
from scipy import constants


# ## Wave-Particle Duality

# ### &#x1f3b2; Particle-like features of light.
# Which of the following phenomena are strongly associated with the particle-like nature of light. <br>
# **A**. Blackbody radiation <br>
# **B**. Compton Scattering  <br>
# **C**. Electron Diffraction <br>
# **D**. Stern-Gerlach Experiment <br>
# **E**. Photoelectric effect 

# In[2]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad1 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad1 = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("The following phenomena are associated with the particle-like nature of light:", ad1)
assert(isinstance(ad1,set) or isinstance(ad1,list) or isinstance(ad1,tuple))
assert(len(ad1) > 0)


# 

# ### &#x1F5A9; Properties of photons
# What is the frequency of light in Hz ($s^{-1}$) of light with wavelength 500 nm?

# In[ ]:


# Use the code box as a calculator, but report your answer as a float. 
# ansDuality2 = float. I've initialized the answer to None.
ad2 = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(ad2,float))


# 

# ### &#x1fa99; Properties of photons
# 
# Doubling the wavelength of radiation doubles its frequency. (True/False)
# 

# In[ ]:


# Report your answer as a Boolean, so freq_double = True or freq_double = False
freq_double = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(freq_double,bool))
print("It is", freq_double, "that when the wavelength of radiation doubles its frequency does also.")


# ### &#x1fa99; Properties of photons
# 
# Doubling the wavelength of radiation halves its speed. (True/False)

# In[ ]:


# Report your answer as a Boolean, so speed_halves = True or speed_halves = False
speed_halves = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(speed_halves,bool))
print("It is", speed_halves, "that when the wavelength of radiation doubles its speed halves.")


# ### &#x1F5A9; Properties of photons
# A helium-neon laser emits light at 632.8 nm.  What is the energy of the photons generated by this laser, in Joules?

# In[ ]:


# Use the code box as a calculator, but report your answer as a float. 
# E_HeNe = float. I've initialized the answer to None.
E_HeNe = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(E_HeNe,float))


# ### &#x1f3b2; Properties of photons
# 
# Which of the following changes would double the energy of a photon: <br>
# **A**. Doubling its frequency <br>
# **B**. Doubling its wavelength <br>
# **C**. Doubling its momentum <br>
# **D**. Doubling its speed <br>
# **E**. Doubling its effective (relativistic) mass <br>
# **F**. Doubling its wavenumber. 

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then e_doubles = ["A", "C"]. 
# I've initialized the answer to the empty list.
e_doubles = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("Ways you can double the energy of a photon include", e_doubles)
assert(isinstance(e_doubles,set) or isinstance(e_doubles,list) or isinstance(e_doubles,tuple))
assert(len(e_doubles) > 0)


# ### &#x1F5A9; Momentum from a green laser pointer
# I have a high-powered green laser pointer (532 nm wavelength, 100 mW power) that I use for astronomical starspotting. If I shine this laser pointer on you, how much momentum, per second, will be transferred to you? Report your answer in SI units of kg m/s.

# In[ ]:


# Use the code box as a calculator, but report your answer as a float. 
# p_greenlaser = float. I've initialized the answer to None.
p_greenlaser = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(p_greenlaser,float))
print("the momentum transfered per second is {0:.3e} kg m/s".format(p_greenlaser))


# ### &#x1F5A9; Wavelength emitted by a radiopharmaceutical
# The radioactive isotope Cobalt-60 is used in nuclear medicine to treat cancer. The energy emitted by Cobalt-60 is 1.29 x 10^11 J/mol. What is the wavelength of the emitted $\gamma$ rays?

# In[ ]:


# Use the code box as a calculator, but report your answer as a float. 
# wlength_Co60 = float. I've initialized the answer to None.
wlength_Co60 = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(wlength_C60,float))


# ### &#x1fa99; Davisson-Germer experiment
# The Davisson-Germer experiment was among the first explicit verifications of the wave-like nature of electrons, and was foundational for modern electron diffraction methods. (True/False)

# In[ ]:


# Report your answer as a Boolean, so ad3 = True or ad3 = False
ad3 = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(ad3,bool))
print("The answer is:", ad3)


# 

# ### &#x1f3b2; Davisson-Germer experiment
# The Davisson-Germer experiment demonstrated that if you shine a beam of electrons on a metal crystal, the result is <br>
# **A**. the electrons are absorbed at “critical energies” similar to the optical (light) absorption spectrum. <br>
# **B**. the electrons scatter according to the Bragg law for X-ray scattering. <br>
# **C**. the electrons go right through the metal. <br>
# **D**. the metal gets very hot and becomes a dull red color (stimulated blackbody emission of radiation). <br>

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad3b = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad3b = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("In the Davisson-Germer experiment", ad3b)
assert(isinstance(ad3b,set) or isinstance(ad3b,list) or isinstance(ad3b,tuple))
assert(len(ad3b) == 1)


# ### &#x1F5A9; Rydberg's Law
# Rydberg's law says that the wavenumber for the absorptions for a one-electron atom/ion with atomic number Z is given by the expression
# $$ \tilde{\nu} = \left( 1.0974 \cdot 10^7 m^{-1}\right) Z^2 
# \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) $$
# where $1 < n_1 < n_2 < \inf$. Suppose you are given the Hydrogen atom in its ground state, $n_1=1$. What is the lowest absorption frequency?

# In[ ]:


# Use the code box as a calculator, but report your answer as a float. 
# ad5 = float. I've initialized the answer to None.
ad5 = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(ad5,float))


# 

# ### &#x1f3b2; Wave properties of particles
# Which of the following experimental results are often cited as examples of the wave-likeness of particles like electrons?  
# **A**. blackbody radiation  
# **B**. discrete emission lines in the hydrogen spectrum  
# **C**. photoelectric effect  
# **D**. Compton scattering of light by a particle  
# **E**. Electron scattering from a crystal

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad6 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad6 = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("The following phenomena are associated with the wave-like nature of electrons:", ad6)
assert(isinstance(ad6,set) or isinstance(ad6,list) or isinstance(ad6,tuple))
assert(len(ad6) > 0)


# ###  &#x1f3b2; Particle properties of waves
# Which of the following experimental results are often cited as examples of the particle-likeness of radiation (light)?   
# **A**. blackbody radiation <br>
# **B**. discrete emission lines in the hydrogen spectrum <br>
# **C**. photoelectric effect <br>
# **D**. Compton scattering of light by a particle <br>
# **E**. Electron scattering from a crystal <br>

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad7 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad7 = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("The following phenomena are associated with the particle-like nature of light:", ad7)
assert(isinstance(ad7,set) or isinstance(ad7,list) or isinstance(ad7,tuple))
assert(len(ad7) > 0)


# In[ ]:


assert(isinstance(momentum_d9,float))
assert(isinstance(frequency_d9,float))


# ### &#x1F5A9; Properties of photons
# What is the momentum and energy of a photon with angular wavenumber $k=10^7 \text{m}^{-1}$?

# In[ ]:


# Use the code box as a calculator, but report your answer as float(s). 
# I've initialized the answers to None.
p_from_k = None   #momentum of the photon
E_from_k = None   #Energy of the photon

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(p_from_k,float))
assert(isinstance(E_from_k,float))


# YOUR ANSWER HERE

# ### &#x1F5A9; De Broglie wavelength of a baseball
# During departmental baseball games, your instructor insists that the only reason he strikes out is because of the De Broglie wavelength of the baseball means that even though he swings in the correct location, he still misses. Suppose that the opposing major-league-quality hurler throws the baseball (mass = 145 g) at 100 miles-per-hour (45 m/s). What is the De Broglie wavelength of the baseball?

# In[ ]:


# Use the code box as a calculator, but report your answer as float(s). 
# I've initialized the answer to None.
wl_baseball = None   #wavelength of the baseball.

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(wl_baseball,float))


# ## The Schr&ouml;dinger Equation

# ### &#x270d;&#xfe0f; Time-Dependent Schr&ouml;dinger Equation
# What is the time-dependent Schr&ouml;dinger equation for the complex conjugate of the wavefunction, $\Psi^*$?
# Put your answer in the markdown cell below. You can drag and drop an attachment (of most types) to this cell also. 

# YOUR ANSWER HERE

# ### &#x1f3b2; Hamiltonian operator
# The Hamiltonian operator corresponds to which observable property of a quantum system? <br>
# **A**. Action <br>
# **B**. Momentum <br>
# **C**. Kinetic Energy <br>
# **D**. De Broglie Wavelength <br>
# **E**. Total Energy <br>
# **F**. Angular Momentum <br>
# **G**. Entropy  
# **H**. Planck Mass

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ansSE2 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ansSE2 = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("The Hamiltonian is the quantum-mechanical operator for:", ansSE2)
assert(isinstance(ansSE2,set) or isinstance(ansSE2,list) or isinstance(ansSE2,tuple))
assert(len(ansSE2) == 1)


# ## Mathematics

# ###  &#x1fa99; Mathematical Properties of the wavefunction
# A probability density can never be negative. (True/False)

# In[ ]:


# Report your answer as a Boolean, so prob_canbe_negative = True or = False
prob_canbe_negative = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(prob_canbe_negative,bool))
print("It is", prob_canbe_negative, "that a probability density can be negative.")


# ### &#x1f3b2; Complex Conjugation
# Let $z$ be a complex number. If $w$ is the product of $z$ and its complex 
# conjugate, $w = z z^*$, which of the following is **always** true about $w$: <br>
# **A**. w is an imaginary number. <br>
# **B**. w is a complex number. <br>
# **C**. w is nonzero real number. <br>
# **D**. w is a nonnegative real number. <br>
# **E**. w is a nonzero complex number. <br>
# **F**. None of the above

# In[ ]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then zzstar = ["A", "C"]. 
# I've initialized the answer to the empty list.
zzstar = []

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print("The product of a number and its complex conjugate is always", zzstar)
assert(isinstance(zzstar,set) or isinstance(zzstar,list) or isinstance(zzstar,tuple))
assert(len(zzstar) > 0)


# ### &#x270d;&#xfe0f; Complex Conjugation
# What is the complex conjugate of 
# $$ \Psi(x,t) = A e^{(a+bi)(kx - \omega t)} $$

# YOUR ANSWER HERE

# ### &#x1fa99; Eigenfunctions of the kinetic-energy operator
# *Every* eigenfunction of the momentum operator is also an eigenfunction of the kinetic-energy operator, and vice versa. (True/False)

# In[ ]:


# Report your answer as a Boolean, so is_also_eigenfunction = True or = False
is_also_eigenfunction = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert(isinstance(is_also_eigenfunction,bool))
print("The answer is:", is_also_eigenfunction)

