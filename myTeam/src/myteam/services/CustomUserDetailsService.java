package com.tdev.myteam.services;

import com.tdev.myteam.domain.User;
import com.tdev.myteam.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class CustomUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(userName);
        if (user == null){
            new UsernameNotFoundException("User does not exist");
        }
        return user;
    }

    @Transactional
    public User loadUserById(int id){
        User user = userRepository.getById(id);
        if (user == null){
            new UsernameNotFoundException("User does not exist");
        }
        return user;
    }
}
